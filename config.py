import os

API_URL = 'http://api.wordnik.com/v4/word.json/'
API_KEY = os.environ['WORDNIK_API_KEY']
ACCESS = {
    'api_key': API_KEY,
    'useCanonical': 'False',
    'type-format': 'ahd'
}

DEBUG = True
SQLALCHEMY_ECHO = True
SECRET_KEY = 'aedfjkg2378rt6wjhdecfbv2734rt623'
REDIS_HOST = os.environ['REDIS_HOST']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
LOC_API = 'http://ip-api.com/json/'