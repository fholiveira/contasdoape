from selenium import webdriver

def url(relative_url = ''):
    return 'http://localhost:5000' + relative_url

def before_all(context):
    context.url = url
    context.browser =  webdriver.Chrome()

def after_all(context):
    context.browser.close()
