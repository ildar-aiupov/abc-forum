from django import template
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from main.models import Post


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def count_post_in_group(group):
    return Post.objects.filter(topic__group=group).count()


@register.filter
def last_post_in_group(group, arg):
    topics = group.Topic.all()
    if not topics.exists():
        return ""
    last_post = Post.objects.filter(topic__in=topics).latest("pub_date")
    if arg == "content":
        return last_post.content
    if arg == "author":
        return last_post.author.username
    if arg == "pub_date":
        return last_post.pub_date
    if arg == "topic_name":
        return last_post.topic.name
    if arg == "url":
        len = last_post.topic.Post.count()
        page_number = len // settings.POSTS_PER_PAGE + 1
        return (
            reverse(
                "main:topic_view",
                kwargs={
                    "topic_id": last_post.topic.id,
                },
            )
            + "?page="
            + str(page_number)
        )


@register.filter
def last_post_in_topic(topic, arg):
    if arg == "url":
        len = topic.Post.count()
        page_number = len // settings.POSTS_PER_PAGE + 1
        return (
            reverse(
                "main:topic_view",
                kwargs={
                    "topic_id": topic.id,
                },
            )
            + "?page="
            + str(page_number)
        )


@register.simple_tag(takes_context=True)
def to_local(context, pub_date):
    request = context["request"]
    if request.user.is_authenticated:
        offset = request.user.utc_offset.offset
    else:
        offset = 3  # для анонимных пользователей - московское время (UTC+3)
    return pub_date + timezone.timedelta(hours=offset)
