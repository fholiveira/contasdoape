from selenium import webdriver
from mongoengine import connect
from usuarios import usuarios

def url(relative_url = ''):
    return 'http://devhost.com:5005' + relative_url

def before_all(context):
    context.database = connect('contasdoape-test')
    context.usuarios = usuarios    
    context.url = url
    context.browser = webdriver.Chrome()

def after_all(context):
    context.browser.close()

def before_scenario(context, scenario):
    context.database.drop_database('contasdoape-test')
