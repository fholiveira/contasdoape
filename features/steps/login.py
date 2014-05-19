from hamcrest import *
from behave import *


@step('que eu não estou logado')
@step('que não estou logado')
@step('que eu sou um novo usuário')
def step_impl(context):
    context.browser.get(context.url('/logoutall'))


@step('eu clicar no botão de login')
def step_impl1(context):
    context.browser.get(context.url('/'))
    context.browser.find_element_by_id('logar').click()


@step('eu devo ser redirecionado para a página de login do Facebook')
def step_impl2(context):
    url = context.browser.current_url
    assert_that(url, starts_with('https://www.facebook.com/login.php'))


@step('eu fizer login como {nome}')
@step('me logo como {nome}')
def passo(context, nome):
    heroi = context.usuarios[nome]

    context.browser.get(context.url())
    context.browser.find_element_by_id('logar').click()

    context.browser.find_element_by_id('email').send_keys(heroi['email'])
    context.browser.find_element_by_id('pass').send_keys(heroi['senha'])

    context.browser.find_element_by_name('login').click()


@step('devo ser direcionado a página de criação de apartamento')
def passo(context):
    url = context.browser.current_url
    assert_that(url, starts_with(context.url('/criar-ape')))


@step("eu clicar no botão 'Vou falar com meus colegas no Facebook'")
def passo(context):
    context.browser.find_element_by_id('redirect_facebook').click()


@step('devo ser redirecionado ao Facebook')
def passo(context):
    url = context.browser.current_url
    assert_that(url, starts_with('https://www.facebook.com'))
