# Generated by Django 4.1.5 on 2023-01-27 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_customuser_is_online"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="last_activity",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
