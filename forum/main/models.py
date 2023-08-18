from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BigGroup(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    # author = models.ForeignKey(
    #     User, related_name="BigGroup", on_delete=models.CASCADE, verbose_name="Автор"
    # )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата опубликования"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")


class Group(models.Model):
    big_group = models.ForeignKey(
        BigGroup,
        related_name="Group",
        on_delete=models.CASCADE,
        verbose_name="Большая группа",
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    # descr = models.CharField(
    #     max_length=200, default="", blank=True, verbose_name="Описание"
    # )
    # author = models.ForeignKey(
    #     User, related_name="Group", on_delete=models.CASCADE, verbose_name="Автор"
    # )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата опубликования"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")


class Topic(models.Model):
    group = models.ForeignKey(
        Group, related_name="Topic", on_delete=models.CASCADE, verbose_name="Группа"
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    first_post = models.TextField(default="", verbose_name="Первое сообщение - текст")
    first_post_image = models.ImageField(
        upload_to="post_images/",
        blank=True,
        verbose_name="Первое сообщение - изображение",
    )
    views_count = models.IntegerField(default=0, verbose_name="Счетчик сообщений")
    author = models.ForeignKey(
        User, related_name="Topic", on_delete=models.CASCADE, verbose_name="Автор"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата опубликования"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        ordering = ["-pub_date"]


class Post(models.Model):
    topic = models.ForeignKey(
        Topic, related_name="Post", on_delete=models.CASCADE, verbose_name="Тема"
    )
    content = models.TextField(default="", verbose_name="Текст")
    image = models.ImageField(
        upload_to="post_images/", blank=True, verbose_name="Изображение"
    )
    author = models.ForeignKey(
        User, related_name="Post", on_delete=models.CASCADE, verbose_name="Автор"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата опубликования"
    )
    is_active = models.BooleanField(default=True, verbose_name="Дата опубликования")

    class Meta:
        ordering = ["pub_date"]
