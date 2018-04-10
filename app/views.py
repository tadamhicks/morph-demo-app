import requests
import os
import json
import redis
from urllib.parse import urlencode
from flask import Flask, request, session, redirect, url_for, \
	render_template, jsonify, make_response
from app import app
from .models import Word_Trie, Word, IpLoc, Location


r = redis.StrictRedis(host=app.config['REDIS_IP'], port=int(app.config['REDIS_PORT']))


@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

'''
This is the autocompleter endpoint.  It uses the check.py complete() method
to look for words already available in redis and suggest them. 
'''
@app.route('/check', methods=['GET'])
def check():
	term = request.args.get('query').lower()
	wt = Word_Trie(r, term)
	results = list(wt.complete(50))
	print(results)
	return jsonify([{'label': x} for x in results])


@app.route('/wordme', methods=['GET'])
def wordme():

	the_word = str(request.args.get('wordage')).lower()
	ip_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) #string
	spot = IpLoc(ip_addr).get_location() #list of floats
	location = Location(the_word, ip_addr, spot[0], spot[1])
	location.create_record()
	others = location.get_records()
	wt = Word_Trie(r, the_word)

	if r.zadd('words', 0 , the_word + '%') == 0:
		'''go get value from mysql
		'''
		word = Word(the_word).get_record()
	else:
		wt.add_word()
		finalUrl = app.config['API_URL'] + the_word + '/pronunciations?%s' % urlencode(app.config['ACCESS'])
		try:
			response = requests.get(finalUrl).json()
			word = response[0]['raw'].strip('()')
		except:
			word = "Could not find word in dictionary"
		entry = Word(the_word, word)
		entry.create_record()

	return render_template('results.html', the_word=the_word, word=word, spot=spot, others=others)