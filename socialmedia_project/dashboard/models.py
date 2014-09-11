from django.db import models
from django.utils.functional import cached_property

# Common Superclasses
from model_utils.models import TimeStampedModel


# Create your models here.
class Event(TimeStampedModel):
    event_occurrence = models.DateTimeField()


class TwitterFollower(TimeStampedModel):
    handle = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    twitter_id = models.IntegerField(unique=True)
    followers_count = models.IntegerField(default=0)
    friends_count = models.IntegerField(default=0)
    description = models.TextField()
    timezone = models.CharField(max_length=100, null=True, blank=True, default="")


class HashTag(TimeStampedModel):
    tag_name = models.CharField(max_length=100)
    last_checked = models.DateTimeField(auto_now_add=True)


class TwitterEvent(Event):
    text = models.TextField()
    tweeted_at = models.DateTimeField()
    tweet_id = models.IntegerField(unique=True)
    happy = models.NullBooleanField(default=None, null=True, blank=True)
    by = models.ForeignKey(TwitterFollower)
    hash_tags = models.ManyToManyField(HashTag)