# Generated by Django 4.1.5 on 2023-01-30 12:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_customuser_last_activity"),
    ]

    operations = [
        migrations.CreateModel(
            name="UtcOffset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("offset", models.IntegerField(default=0)),
                ("description", models.CharField(default="", max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="utc_offset",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="users.utcoffset",
                verbose_name="Часовой пояс",
            ),
            preserve_default=False,
        ),
    ]
