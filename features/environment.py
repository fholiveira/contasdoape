from ThreadedServer import ThreadedServer
from mongoengine import connect
from selenium import webdriver
from usuarios import usuarios
from os import environ


def url(relative_url=''):
    return 'http://devhost.com:5005' + relative_url


def before_all(context):
    environ['CONTASDOAPE_ENV'] = 'TESTING'
    from contasdoape.web import app

    context.server = ThreadedServer(app, host='devhost.com', port=5005)
    context.server.start()

    context.database = connect('contasdoape-test')
    context.usuarios = usuarios
    context.url = url


def before_feature(context, feature):
    if 'firefox' in feature.tags:
        context.browser = webdriver.Firefox()
    else:
        context.browser = webdriver.Chrome()


def after_feature(context, feature):
    context.browser.close()


def before_scenario(context, scenario):
    context.database.drop_database('contasdoape-test')


def after_all(context):
    context.server.stop()
