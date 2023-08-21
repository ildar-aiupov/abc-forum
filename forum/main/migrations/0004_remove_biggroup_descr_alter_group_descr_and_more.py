# Generated by Django 4.1.5 on 2023-01-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_views_number_topic_views_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="biggroup",
            name="descr",
        ),
        migrations.AlterField(
            model_name="group",
            name="descr",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(verbose_name="Текст сообщения"),
        ),
        migrations.AlterField(
            model_name="topic",
            name="first_post",
            field=models.TextField(default="", verbose_name="Первое сообщение темы"),
        ),
        migrations.AlterField(
            model_name="topic",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Название темы"),
        ),
    ]
