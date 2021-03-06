from json import JSONEncoder, JSONDecoder
from tweepy import API, OAuthHandler, TweepError
import os

def loadfile(mode):
    if os.name == 'nt':
        home_path = os.path.expanduser('~{0}'.format(os.environ['USERNAME']))
    elif os.name == 'posix':
        home_path = os.environ['HOME']
    f = open('{0}/.wtweet'.format(home_path), mode)
    return f

class WTweetUser:
    def __init__(self):
        _CONSUMER_KEY = '9o4scrLHTFt7NzyVxD5Q'
        _CONSUMER_SECRET = 'xlrPmai1QgNTRQTf86inp1bzEFLgEXD7XuN5ZENKAU'
        self.__auth_handler = OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
        self.__access_token = None

    def set_access_token(self, access_token):
        self.__access_token = self.__auth_handler.set_access_token(key=access_token['key'], secret=access_token['secret'])

    def get_auth_handler(self):
        return self.__auth_handler

    def logout(self):
        with loadfile('w') as f:
            f.truncate()
            f.close()
        print 'logout successful!'

    def login(self):
        try:
            auth_url = self.__auth_handler.get_authorization_url()
            print 'give me a pin code from url: {0}'.format(auth_url)
            verifier = raw_input('enter a pin code: ').strip()
            self.__auth_handler.get_access_token(verifier=verifier)
            access_token = { 'key': self.__auth_handler.access_token.key, 'secret': self.__auth_handler.access_token.secret }

            with loadfile('w+') as f:
                f.truncate()
                f.write(JSONEncoder().encode(access_token))
                f.close()
        except TweepError as err:
            print err.__str__()

        return WTweetTimeline(self)

    def is_login(self):
        with loadfile('r') as f:
            cfg = f.readline()
            f.close()
        access_token = JSONDecoder().decode(cfg)

        if 'key' in access_token and 'secret' in access_token:
            self.set_access_token(access_token=access_token)
            return True
        else:
            return False

    def get_timeline(self):
        with loadfile('r') as f:
            cfg = f.readline()
            f.close()
        self.set_access_token(JSONDecoder().decode(cfg))
        return WTweetTimeline(self)

class WTweetTimeline:
    def __init__(self, wtweet_user):
        self.api = API(wtweet_user.get_auth_handler())

    def tweet(self, message=''):
        self.api.update_status(message)

def main():
    import sys

    if sys.argv[1] == 'login':
        user = WTweetUser().login()
    elif sys.argv[1] == 'logout':
        user = WTweetUser().logout()
    else:
        if WTweetUser().is_login():
            user = WTweetUser().get_timeline()

        user.tweet(sys.argv[1])

    return 0
