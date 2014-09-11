import datetime
import time
from email.utils import parsedate
from twitter import *

__author__ = 'tmehta'

# it's about time to create a TwitterSearch object with our secret tokens
t = Twitter(auth=OAuth('1363462640-Bwrpds3AK7UeCqEmvkrABfKdGfqzgl9pO3hJ1mk',
                       '7SFgvvflEchJxgyePZwiwQV6CYC7H7joVbSh8bjZM', 'phYQOWa0275clxNNPRz0rw',
                       '0vvkv6vGm2G9o1tLMtyn7KzObcmKEaMmK2MeAz3DdSw'))


def get_by_hash_tag(hash_tag, since_inner=datetime.datetime.today()):
    q = hash_tag
    oldest_id = TwitterEvent.objects.order_by('tweet_id')[0].tweet_id
    for twe in t.search.tweets(q=q, count=1000, since_id=oldest_id, result_type='recent')[
        'statuses']:
        # GET OR CREATE FOLLOWER
        try:
            TwitterEvent.objects.get(tweet_id=twe['id'])
        except TwitterEvent.DoesNotExist:
            try:
                follower = TwitterFollower.objects.get(twitter_id=twe['user']['id'])
            except TwitterFollower.DoesNotExist:
                print "Creating follower"
                follower = TwitterFollower.objects.create(twitter_id=twe['user']['id'],
                                                          followers_count=twe['user']['followers_count'],
                                                          description=twe['user']['description'],
                                                          friends_count=twe['user']['friends_count'],
                                                          handle=twe['user']['screen_name'],
                                                          timezone=twe['user']['time_zone'])
            # TODO: Update follower
            # Create Tweet
            date = datetime.datetime.fromtimestamp(time.mktime(parsedate(twe['created_at'])))
            tw = TwitterEvent.objects.create(text=twe['text'], tweeted_at=date,
                                             event_occurrence=date,
                                             tweet_id=twe['id'], by=follower)
            # TODO: Multiple Hash tags
            tw.hash_tags = [HashTag.objects.get(tag_name=hash_tag).id]
            tw.save()


if __name__ == "__main__":
    since = datetime.datetime.today()
    since = since - datetime.timedelta(days=1)
    for tweet in t.search.tweets(q='lvg', count=1, since=since.strftime('%Y-%m-%d'))['statuses']:
        # GET OR CREATE FOLLOWER
        print tweet
else:
    from dashboard.models import TwitterFollower, HashTag
    from dashboard.models import TwitterEvent

    for tag in HashTag.objects.all():
        print tag.tag_name
        get_by_hash_tag(tag.tag_name)