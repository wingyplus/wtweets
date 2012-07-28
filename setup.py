from setuptools import setup, find_packages
setup(
    name = 'wtweets',
    version = '2.0',
    packages = find_packages(),

    author = 'Thanabodee C.',
    author_email = 'wingyminus@gmail.com',
    description = 'twitter cli for geeks :-D',
    keywords = 'twitter tweet twt',

    scripts = ['wtweet'],
    install_requires = ['tweepy>=1.10'],
    entry_points = {
        'console_scripts' : [ 'wtweet = wtweets.tweet:main' ]
    }

)
