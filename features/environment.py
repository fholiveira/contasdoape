from selenium import webdriver
from mongoengine import connect
from usuarios import usuarios


def url(relative_url=''):
    return 'http://devhost.com:5005' + relative_url


def before_all(context):
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
