# Generated by Django 4.1.5 on 2023-01-25 15:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topic",
            old_name="views_number",
            new_name="views_count",
        ),
    ]
