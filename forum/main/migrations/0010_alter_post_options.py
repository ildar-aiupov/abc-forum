# Generated by Django 4.1.5 on 2023-08-18 14:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_remove_biggroup_author_remove_group_author_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["pub_date"]},
        ),
    ]
