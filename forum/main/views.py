from django.core.paginator import Paginator
from django.db.models import Count, Max
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from main.forms import TopicCreateForm, PostCreateForm
from main.models import BigGroup, Group, Topic, Post, User


tree = {}


def get_paginated_page(items_list, page_number, items_per_page):
    paginator = Paginator(items_list, items_per_page)
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_tree(group=None, topic=None, dontclear=None):
    if not dontclear:
        tree.clear()
    if topic:
        tree["Тема: " + topic.name] = reverse(
            "main:topic_view", kwargs={"topic_id": topic.id}
        )
        group = topic.group
    if group:
        tree["Группа: " + group.name] = reverse(
            "main:group_view",
            kwargs={"group_id": group.id, "order_method": "order_topic_later"},
        )
        tree["Форум: " + group.big_group.name] = reverse("main:index")
    tree["Все форумы"] = reverse("main:index")
    return dict(reversed(tree.items()))


def get_safe_content(content: str):
    # уничтожаем тэги html, потом некоторые тэги восстанавливаем или преобразуем
    return (
        content.replace("<", "&le;")
        .replace("&le;quote>", "<quote>")
        .replace("&le;/quote>", "</quote>")
        .replace("&le;start_text>", "<br>")
        .replace("\n", "<br>")
    )


def index(request):
    big_groups = BigGroup.objects.all()
    context = {
        "tree": get_tree(),
        "big_groups": big_groups,
    }
    return render(request, "index.html", context)


def group_view(request, group_id, order_method):
    group = get_object_or_404(Group, id=group_id)
    order_methods = {
        "order_topic_later": "-pub_date",
        "order_topic_earlier": "pub_date",
        "order_views_more": "-views_count",
        "order_views_less": "views_count",
        "order_posts_more": "-posts_count",
        "order_posts_less": "posts_count",
        "order_last_post_later": "-last_post",
        "order_last_post_earlier": "last_post",
    }
    topics = (
        Topic.objects.filter(group=group_id)
        .annotate(posts_count=Count("Post"), last_post=Max("Post__pub_date"))
        .order_by(order_methods[order_method])
    )
    page_number = request.GET.get("page")
    page_obj = get_paginated_page(topics, page_number, settings.TOPICS_PER_PAGE)
    # обрабатываем форму
    form = TopicCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.user.is_authenticated:
        # создаем тему
        new_topic = form.save(commit=False)
        new_topic.author = request.user
        new_topic.group = Group.objects.get(id=group_id)
        new_topic.save()
        # создаем первое сообщение темы
        Post.objects.create(
            topic=new_topic,
            author=request.user,
            content=new_topic.first_post,
            image=new_topic.first_post_image,
        )
        # увеличим счетчик сообщений пользователя
        request.user.post_count += 1
        request.user.save()
        return redirect("main:topic_view", new_topic.id)

    context = {
        "tree": get_tree(group=group),
        "group": group,
        "page_obj": page_obj,
        "form": form,
        "order_method": order_method,
    }
    return render(request, "group_view.html", context)


def topic_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(topic=topic_id)
    page_number = request.GET.get("page")
    page_obj = get_paginated_page(posts, page_number, settings.TOPICS_PER_PAGE)
    # увеличим счетчик просмотров темы
    if request.method == "GET":
        topic.views_count += 1
        topic.save()
    # обрабатываем форму
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.user.is_authenticated:
        # создаем новое сообщение
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.topic = Topic.objects.get(id=topic_id)
        new_post.content = get_safe_content(new_post.content)
        new_post.save()
        # увеличим счетчик сообщений пользователя
        request.user.post_count += 1
        request.user.save()
        # вернуться на страницу, вызвавшую этот метод
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        # return redirect("main:topic_view", topic.id)
    context = {
        "tree": get_tree(topic=topic),
        "topic": topic,
        "page_obj": page_obj,
        "form": form,
        "request": request,
    }
    return render(request, "topic_view.html", context)


def today_posts(request):
    # определяем часовой пояс пользователя; для анонимного будет МСК (UTC+3)
    offset = request.user.utc_offset.offset if request.user.is_authenticated else 3
    local_datetime = timezone.now() + timezone.timedelta(hours=offset)
    local_midnight_offset = timezone.timedelta(
        hours=local_datetime.hour
    ) + timezone.timedelta(minutes=local_datetime.minute)
    utc_passed_point = timezone.now() - local_midnight_offset
    today_posts = Post.objects.filter(pub_date__gt=utc_passed_point)
    today_posts_topics = Topic.objects.filter(Post__in=today_posts).distinct()
    page_number = request.GET.get("page")
    page_obj = get_paginated_page(
        today_posts_topics, page_number, settings.TOPICS_PER_PAGE
    )
    context = {
        "page_obj": page_obj,
        "tree": get_tree(dontclear=True),
    }
    return render(request, "today_posts.html", context)


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        "user": user,
        "tree": get_tree(),
    }
    return render(request, "user_profile.html", context)


def active_users(request):
    active_users = User.objects.filter(is_online=True)
    context = {
        "active_users": active_users,
        "tree": get_tree(dontclear=True),
    }
    return render(request, "active_users.html", context)


def about_author(request):
    context = {
        "tree": get_tree(dontclear=True),
    }
    return render(request, "about_author.html", context)


def rules(request):
    context = {
        "tree": get_tree(dontclear=True),
    }
    return render(request, "rules.html", context)
