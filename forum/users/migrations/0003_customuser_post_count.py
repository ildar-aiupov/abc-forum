# Generated by Django 4.1.5 on 2023-01-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="post_count",
            field=models.IntegerField(default=0),
        ),
    ]
