from mongoengine import connect
from flask import Flask, abort, session
from flask.ext.login import LoginManager
from os import path,getcwd

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

config_file = 'producao.cfg' if path.isfile('contasdoape/producao.cfg') else 'desenv.cfg'
app.config.from_pyfile(config_file)

connect(app.config['DB_NAME'])

from contasdoape.views import login
#from contasdoape.views import despesa
from contasdoape.views import sumario 
