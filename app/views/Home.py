from bottle import TEMPLATE_PATH, route, jinja2_template as template
from app.models import *

TEMPLATE_PATH.append('./templates')

@route('/')
def home():
    return template('home.html')
