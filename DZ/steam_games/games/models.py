from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Game(models.Model):
    name = models.CharField(max_length=255)
    app_id = models.IntegerField(unique=True)
    playtime_forever = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    steam_id = models.CharField(max_length=50, unique=True)
    avatar_url = models.URLField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nickname} ({self.steam_id})"
