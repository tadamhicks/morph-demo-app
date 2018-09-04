from app import app, db
import requests
import json
from sqlalchemy.exc import IntegrityError


'''
Word_Trie sets up the data structure for the autocomplete API.  Creates a
trie for each word on addition.
'''
class Word_Trie(object):

	def __init__(self, r, word):

		self.r = r
		self.word = word


	def add_word(self):
		
		for l in range(1, len(self.word)):
			prefix = self.word[0:l]
			self.r.zadd('words', 0, prefix)
		
		self.r.zadd('words', 0, self.word+'%')


	def complete(self, count):
		
		results = set()
		grab = 42
		start = self.r.zrank('words', self.word)
		
		if not start:
			return results
		
		while (len(results) != count):
			range = self.r.zrange('words', start, start+grab-1)
			start += 1
			
			if not range or len(range) == 0:
				break
			
			for entry in range:
				entry = entry.decode("utf-8")
				minlen = min(len(entry), len(self.word))
				
				if entry[0:minlen] != self.word[0:minlen]:
					count = len(results)
					break
				
				if entry[-1] == "%" and len(results) != count:
					results.add(entry[0:-1])
		
		return results


class IpLoc(object):

	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def get_location(self):

		response = requests.get('http://ip-api.com/json/' + self.ip_addr)
		json_data = json.loads(response.text)
		try:
			lat = json_data['lat']
			lon = json_data['lon']
		except:
			lat = 0
			lon = 0
		return [lat, lon]


'''
To make things easy we store previously searched words and their phonetic spelling.
Word is a pair of the submitted word to the phonetic spelling.
'''
class Word(db.Model):

	__tablename__ = 'word'
	wordage = db.Column(db.String(128), index=True, unique=True, primary_key=True)
	phone_spell = db.Column(db.String(128))

	def __init__(self, wordage=None, phone_spell=None):

		self.wordage = wordage
		self.phone_spell = phone_spell

	def create_record(self):

		db.session.add(self)
		db.session.commit()

	def get_record(self):

		return Word.query.get(self.wordage).phone_spell


'''
We also need to keep track of the word as it relates to previous searches and the
location of the searcher
'''
class Location(db.Model):

	__tablename__ = 'location'
	wordage = db.Column(db.String(128), index=True, primary_key=True)
	ip_address = db.Column(db.String(128), primary_key=True)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)

	def __init__(self, wordage=None, ip_address=None, latitude=None, longitude=None):

		self.wordage = wordage
		self.ip_address = ip_address
		self.latitude = latitude
		self.longitude = longitude

	def create_record(self):

		try:
			db.session.add(self)
			db.session.commit()

		except IntegrityError:
			db.session.rollback()

	def get_records(self):
		return Location.query.filter(Location.wordage == self.wordage).all()
