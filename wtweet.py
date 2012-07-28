# -*- coding: utf-8 -*-
from tweepy import OAuthHandler, TweepError, API

class TwitterUser:
    pass

class TwitterTimeline:
    def __init__(self):
        pass

    def tweet(message=''):
        pass

if __name__ == '__main__':
    import sys, os
    from json import JSONEncoder, JSONDecoder
    # tweet_msg = sys.argv[1]

    CONSUMER_KEY = '9o4scrLHTFt7NzyVxD5Q'
    CONSUMER_SECRET = 'xlrPmai1QgNTRQTf86inp1bzEFLgEXD7XuN5ZENKAU'

    try:
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

        if sys.argv[1] == 'config':
            auth_url = auth.get_authorization_url()
            print auth_url
            verifier = raw_input('PIN: ').strip()
            auth.get_access_token(verifier=verifier)
            access_token = { 'key': auth.access_token.key, 'secret': auth.access_token.secret }
            f = open('{0}/.wtweet'.format(os.environ['HOME']), 'w+')
            f.write(JSONEncoder().encode(access_token))
            f.close()
        else:
            f = open('{0}/.wtweet'.format(os.environ['HOME']), 'r')
            cfg = f.readline()
            f.close()
            access_token = JSONDecoder().decode(cfg)
            auth.set_access_token(key=access_token['key'], secret=access_token['secret'])
            api = API(auth)
            api.update_status(sys.argv[1])
    except TweepError as err:
        print 'Error: ', err.__str__()

