# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import beeline
from beeline.middleware.flask import HoneyMiddleware
from beeline.patch.requests import *

from opentelemetry.instrumentation.flask import FlaskInstrumentor

# db variable initialization

app = Flask(__name__)
app.config.from_object('config')

beeline.init(writekey=app.config['HONEYCOMB_API_KEY'], dataset=app.config['HONEYCOMB_DATASET'], service_name=app.config['SERVICE_NAME'])

db = SQLAlchemy(app)
HoneyMiddleware(app, db_events=True)


from app import views, models

#FlaskInstrumentor().instrument_app(app)
