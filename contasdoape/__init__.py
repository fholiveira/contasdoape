from rauth.service import OAuth2Service
from mongoengine import connect
from flask import Flask
from os import path,getcwd

app = Flask(__name__)

config_file = 'producao.cfg' if path.isfile('contasdoape/producao.cfg') else 'desenv.cfg'
app.config.from_pyfile(config_file)

connect(app.config['DB_NAME'])

graph_url = 'https://graph.facebook.com/'
facebook = OAuth2Service(name='facebook',
                         authorize_url='https://www.facebook.com/dialog/oauth',
                         access_token_url=graph_url + 'oauth/access_token',
                         client_id=app.config['FB_CLIENT_ID'],
                         client_secret=app.config['FB_CLIENT_SECRET'],
                         base_url=graph_url)

from contasdoape.views import despesa
from contasdoape.views import sumario 
from contasdoape.views import login
