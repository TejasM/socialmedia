from django.contrib.auth.models import User
from django.db import models

# Common Superclasses
from model_utils.models import TimeStampedModel


class TwitterFollower(TimeStampedModel):
    handle = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    twitter_id = models.BigIntegerField(unique=True)
    followers_count = models.IntegerField(default=0)
    friends_count = models.IntegerField(default=0)
    description = models.TextField()
    timezone = models.CharField(max_length=100, null=True, blank=True, default="")


frequencies = [('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')]


class UserSpec(models.Model):
    hash_tag = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    frequency = models.CharField(choices=frequencies, max_length=1)


class UserProfile(models.Model):
    company_name = models.CharField(max_length=1000)
    user = models.OneToOneField(User)


class Tweet(models.Model):
    text = models.TextField()
    retweets = models.IntegerField(default=0)
    tweeted_at = models.DateTimeField()
    tweet_id = models.BigIntegerField(unique=True)
    sentiment = models.TextField()
    by = models.ForeignKey(TwitterFollower)
    spec = models.ForeignKey(UserSpec)