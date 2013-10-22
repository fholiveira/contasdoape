from flask import Flask
from mongoengine import connect

app = Flask(__name__)
connect('contasdoape')

from contasdoape.views import despesa
from contasdoape.views import sumario 
