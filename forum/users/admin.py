from django.contrib import admin

from .models import CustomUser, UtcOffset


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "post_count",
        "is_online",
        "last_activity",
        "utc_offset",
    )


@admin.register(UtcOffset)
class UtcOffsetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "offset",
    )
