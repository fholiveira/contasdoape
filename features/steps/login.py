from behave import *
from selenium import webdriver
from selenium.webdriver.support import ui

driver = webdriver.Chrome()

@given('que eu não estou logado')
def step_impl(context):
    driver.get('http:\\localhost:5000')

@when('eu clicar no botão de login')
def step_impl1(context):
    botao = driver.find_element_by_id('logar')
    botao.click()

@then('eu devo ser redirecionado para a página de login do Facebook')
def step_impl2(context):
    print (driver.current_url)
    assert driver.current_url.startswith('https://www.facebook.com/login.php')
    driver.close()
