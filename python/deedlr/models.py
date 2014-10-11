from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    hashtag = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return self.hashtag


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    preferred_categories = models.ManyToManyField(Category, blank=True, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    rank = models.PositiveSmallIntegerField(default=1)
    last_seen_location = models.PointField(geography=True, null=True, blank=True)
    last_seen_timestamp = models.DateTimeField(null=True)
