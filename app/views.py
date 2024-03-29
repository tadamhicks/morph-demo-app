from typing import Any
from urllib.parse import urlencode

import redis
import requests
from flask import request, render_template, jsonify

from app import app
from .models import WordTrie, Word, IpLoc, Location
import beeline

'''
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from grpc import ssl_channel_credentials


resource = Resource(attributes={
    "service.name": app.config['SERVICE_NAME']
})
trace_provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="api.honeycomb.io:443",
    insecure=False,
    credentials=ssl_channel_credentials(),
    headers=(
        ("x-honeycomb-team", app.config['HONEYCOMB_API_KEY']),
        ("x-honeycomb-dataset", app.config['HONEYCOMB_DATASET'])
    )
)

trace_provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

trace.set_tracer_provider(trace_provider)

tracer = trace.get_tracer(__name__)
'''
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

	beeline.add_context_field("word", term)
	wt = WordTrie(r, term)
	results: list[Any] = list(wt.complete(50))
	print(results)
	return jsonify([{'label': x} for x in results])


@app.route('/wordme', methods=['GET'])
def wordme():

	the_word = str(request.args.get('wordage')).lower()
	beeline.add_context_field('word', the_word)
	ip_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  # string
	spot = IpLoc(ip_addr).get_location()  # list of floats
	location = Location(the_word, ip_addr, spot[0], spot[1])
	location.create_record()
	others = location.get_records()
	wt = WordTrie(r, the_word)

	if r.zadd('words', {the_word + '%': 0}) == 0:
		'''go get value from mysql
		'''
		word = Word(the_word).get_record()
	else:
		wt.add_word()
		final_url = app.config['API_URL'] + the_word + '/pronunciations?%s' % urlencode(app.config['ACCESS'])
		try:
			response = requests.get(final_url).json()
			word = response[0]['raw'].strip('()')
		except:
			word = "Could not find word in dictionary"
		entry = Word(the_word, word)
		entry.create_record()

	return render_template('results.html', the_word=the_word, word=word, spot=spot, others=others)
