from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(
        upload_to="users_avatars/", blank=True, verbose_name="Изображение"
    )
    post_count = models.IntegerField(default=0, verbose_name="Счетчик сообщений")
    is_online = models.BooleanField(default=False, verbose_name="Онлайн")
    last_activity = models.DateTimeField(
        auto_now_add=True, verbose_name="Последняя активность"
    )
    utc_offset = models.ForeignKey(
        "UtcOffset", on_delete=models.CASCADE, null=True, verbose_name="Часовой пояс"
    )


class UtcOffset(models.Model):
    offset = models.IntegerField(default=3, verbose_name="Смещение")
    description = models.CharField(
        default="MSK+0", max_length=20, verbose_name="Описание"
    )

    def __str__(self):
        return self.description
