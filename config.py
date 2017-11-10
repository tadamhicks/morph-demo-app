import os

API_URL = 'http://api.wordnik.com/v4/word.json/'
API_KEY = os.environ['WORDNIK_API_KEY']
ACCESS = {'api_key': API_KEY, 'useCanonical': 'False', 'type-format': 'ahd'}

if os.environ['ENVIRONMENT'] == 'dev':
	DEBUG = True
	SQLALCHEMY_ECHO = True
else:
	DEBUG = False
	SQLALCHEMY_ECHO = False

SECRET_KEY = 'aedfjkg2378rt6wjhdecfbv2734rt623'
REDIS_IP = os.environ['REDIS_IP']
REDIS_PORT = os.environ['REDIS_PORT']
SQLA_DB_USER = os.environ['MYSQL_USERNAME']
SQLA_DB_PASSWORD = os.environ['MYSQL_PASSWORD']
SQLA_DB_HOST = os.environ['MYSQL_IP']
SQLA_DB_PORT = os.environ['MYSQL_PORT']
SQLA_DB_NAME = os.environ['DB_NAME']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + SQLA_DB_USER + ':' + SQLA_DB_PASSWORD + '@' + SQLA_DB_HOST + ':' + SQLA_DB_PORT + '/' + SQLA_DB_NAME
LOC_API = 'http://ip-api.com/json/'