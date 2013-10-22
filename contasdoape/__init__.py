from flask import Flask
from mongoengine import connect

app = Flask(__name__)
connect('contasdoape')

from .views  import despesa
