# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import beeline
#from beeline.middleware.flask import HoneyMiddleware
#from beeline.patch.requests import *

from opentelemetry.instrumentation.flask import FlaskInstrumentor

# db variable initialization

#beeline.init(writekey='c4b05d6b2259d9d6fca768d4ba9c811a', dataset="demo-app", service_name="demo-app-svc")

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
#HoneyMiddleware(app)


from app import views, models

FlaskInstrumentor().instrument_app(app)
