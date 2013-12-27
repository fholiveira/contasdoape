from behave import *

@given('que eu não estou logado')
def step_impl(context):
    context.browser.get(context.url())

@when('eu clicar no botão de login')
def step_impl1(context):
    context.browser.find_element_by_id('logar').click()

@then('eu devo ser redirecionado para a página de login do Facebook')
def step_impl2(context):
    assert context.browser.current_url.startswith('https://www.facebook.com/login.php')

@given('que eu sou um novo usuário')
def passo(context):
    context.browser.get(context.url('/logout'))

@when('eu fizer login com {usuario} e {senha}')
def passo(context, usuario, senha):
    context.browser.get(context.url())
    botao = context.browser.find_element_by_id('logar')
    botao.click()

    mail = context.browser.find_element_by_id('email')
    mail.send_keys(usuario)
    pwd = context.browser.find_element_by_id('pass')
    pwd.send_keys(senha)

    context.browser.find_element_by_name('login').click()

@then('devo ser direcionado a página de criação de apartamento')
def passo(context):
    url = context.browser.current_url 
    assert url == context.url('/primeiros_passos')
