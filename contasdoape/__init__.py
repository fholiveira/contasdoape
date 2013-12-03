from flask import Flask
from mongoengine import connect
from os import path

app = Flask(__name__)

config_file = 'producao.cfg' if path.isfile('producao.cfg') else 'desenv.cfg'
app.config.from_pyfile(config_file)

connect(app.config['DB_NAME'])

from contasdoape.views import despesa
from contasdoape.views import sumario 
