from mongoengine import connect
from flask import Flask, abort, session
from flask.ext.login import LoginManager
from os import path, getcwd, environ, listdir
from contasdoape.environments import Environments

def load_envs():
    diretorio = 'contasdoape/config'
    env = Environments(app, var_name='CONTASDOAPE_ENV')
    arquivos = [arquivo for arquivo in listdir(diretorio)
                if path.isfile(path.join(diretorio, arquivo))]

    for arquivo in arquivos:
        env.from_yaml(path.join(diretorio, arquivo))

app = Flask(__name__)

load_envs()

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
