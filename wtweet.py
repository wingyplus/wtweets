# -*- coding: utf-8 -*-
from tweepy import OAuthHandler, TweepError, API

if __name__ == '__main__':
    import sys
    # tweet_msg = sys.argv[1]

    CONSUMER_KEY = '9o4scrLHTFt7NzyVxD5Q'
    CONSUMER_SECRET = 'xlrPmai1QgNTRQTf86inp1bzEFLgEXD7XuN5ZENKAU'

    try:
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth_url = auth.get_authorization_url()
        print auth_url
        verifier = raw_input('PIN: ').strip()
        auth.get_access_token(verifier=verifier)
        api = API(auth)
        api.update_status('@Breeze_Pornthip เล่น tweepy')
    except TweepError as err:
        print 'Error: ', err.__str__()



