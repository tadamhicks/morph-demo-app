import os


def create_file():
	f = open('config.py', 'w')

	API_URL = 'http://api.wordnik.com/v4/word.json/'
	API_KEY = os.environ['WORDNIK_API_KEY']
	ACCESS = {
	    'api_key': API_KEY,
	    'useCanonical': 'False',
	    'type-format': 'ahd'
	}


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
	SQLA_DB_NAME = os.environ['SQLA_DB_NAME']
	#SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+SQLA_DB_USER+':'\
	    +SQLA_DB_PASSWORD+'@'+SQLA_DB_HOST+'/'+SQLA_DB_NAME

	LOC_API = 'http://ip-api.com/json/'

	f.write(
		'API_URL = ' + repr(API_URL) + '\n'
		'API_KEY = ' + repr(API_KEY) + '\n'
		'ACCESS = ' + repr(ACCESS) + '\n'
		'DEBUG = ' + repr(DEBUG) + '\n'
		'SQLALCHEMY_ECHO = ' + repr(SQLALCHEMY_ECHO) + '\n'
		'SECRET_KEY = ' + repr(SECRET_KEY) + '\n'
		'REDIS_IP = ' + repr(REDIS_IP) + '\n'
		'REDIS_PORT = ' + repr(REDIS_PORT) + '\n'
		'SQLA_DB_USER = ' + repr(SQLA_DB_USER) + '\n'
		'SQLA_DB_PASSWORD = ' + repr(SQLA_DB_PASSWORD) + '\n'
		'SQLA_DB_HOST = ' + repr(SQLA_DB_HOST) + '\n'
		'SQLA_DB_NAME = ' + repr(SQLA_DB_NAME) + '\n'
		'SQLALCHEMY_DATABASE_URI = ' + repr(SQLALCHEMY_DATABASE_URI) + '\n'
		'LOC_API = ' + repr(LOC_API) + '\n'
		)

if __name__ == "__main__":
	create_file()