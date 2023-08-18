from django.contrib import admin

from main.models import BigGroup, Group, Topic, Post


@admin.register(BigGroup)
class BigGroupAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "pub_date",
        "is_active",
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "big_group",
        "name",
        "pub_date",
        "is_active",
    )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "group",
        "author",
        "pub_date",
        "is_active",
        "name",
        "views_count",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "topic",
        "author",
        "pub_date",
        "is_active",
        "content",
    )
