from contasdoape.environments import Environments
from flask.ext.login import LoginManager
from mongoengine import connect
from flask import Flask

app = Flask(__name__)

Environments(app, var_name='CONTASDOAPE_ENV') \
    .from_yaml('contasdoape/conf.yaml')

login_manager = LoginManager()
login_manager.init_app(app)

if app.config.get('MONGO', None):
    connect(app.config['MONGO'])
else:
    connect(app.config['MONGO_DATABASE'],
            username=app.config['MONGO_USERNAME'],
            password=app.config['MONGO_PASSWORD'],
            host=app.config['MONGO_HOST'],
            port=app.config['MONGO_PORT'])

from contasdoape.views import *
