from mongoengine import connect
from flask import Flask, abort, session
from flask.ext.login import LoginManager
from os import path, getcwd, environ, listdir
from contasdoape.environments import Environments

app = Flask(__name__)

Environments(app, var_name='CONTASDOAPE_ENV').from_yaml('contasdoape/conf.yaml')

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

from contasdoape.views import ape
from contasdoape.views import login
from contasdoape.views import sumario 
from contasdoape.views import despesa
from contasdoape.views import relatorio 
