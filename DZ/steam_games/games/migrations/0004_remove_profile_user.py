# Generated by Django 4.2.16 on 2024-12-08 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_rename_avatar_profile_avatar_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
    ]
