# Generated by Django 4.1.5 on 2023-02-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="post_images/", verbose_name="Изображение"
            ),
        ),
    ]
