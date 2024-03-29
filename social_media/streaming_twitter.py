import time
from dashboard.models import Tweet, TwitterFollower, UserSpec

__author__ = 'tmehta'
from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            user_id = data['user']['id']
            try:
                follower = TwitterFollower.objects.get(twitter_id=user_id)
            except TwitterFollower.DoesNotExist:
                description = ''
                if data['user']["description"]:
                    description = data['user']["description"]
                follower = TwitterFollower.objects.create(twitter_id=user_id, handle=data['user']['screen_name'],
                                                          name=data['user']['name'],
                                                          followers_count=data['user']["followers_count"],
                                                          friends_count=data['user']["friends_count"],
                                                          description=description)
            spec = None
            for tag in data['entities']['hashtags']:
                try:
                    spec = UserSpec.objects.get(hash_tag=tag['text'].lower())
                    print "Got", tag
                except:
                    print "Didn't Get", tag
            if spec:
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                Tweet.objects.create(text=data['text'], retweets=data['retweet_count'], tweeted_at=ts,
                                     tweet_id=data['id'], by=follower, spec=spec)
                print "Tweet created"

    def on_error(self, status_code, data):
        print status_code
        # self.disconnect()


stream = MyStreamer('UR7PSstYAPjRpHGJV3DfTKHjX', 'cIJjcRHjrga5umsPp6iGWi0RFhgDUIybieg8XyvmEj0CkAn1PZ',
                    '1363462640-l9AXw6jpKv3d3MzddqHVY3BV16l3dz2596mg0dZ',
                    'qRqns6173zX9jNDJOwqTDCe6BNSSr2ybB4pzrdr3Tbpzh')
stream.statuses.filter(track='wethenorth')