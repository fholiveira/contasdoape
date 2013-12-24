from behave import *

@given('que eu não estou logado')
def step_impl(context):
    context.browser.get('http:\\localhost:5000')

@when('eu clicar no botão de login')
def step_impl1(context):
    botao = context.browser.find_element_by_id('logar')
    botao.click()

@then('eu devo ser redirecionado para a página de login do Facebook')
def step_impl2(context):
    assert context.browser.current_url.startswith('https://www.facebook.com/login.php')
