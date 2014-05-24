from hamcrest import *
from behave import *


@step('estou na página de lançar despesas')
@step('que estou na página de lançar despesas')
def passo(context):
    context.browser.get(context.url('/despesas/nova'))


@step('que eu não preenchi os campos')
def passo(context):
    context.browser.find_element_by_id('data').clear()
    context.browser.find_element_by_id('valor').clear()
    context.browser.find_element_by_id('descricao').clear()


@step('eu clico no botão "Lançar"')
def passo(context):
    context.browser.find_element_by_id('lancar').click()


@step('clico no botão "Lançar"')
def passo(context):
    context.browser.find_element_by_id('lancar').click()


@step('o campo "{nome}" deve indicar um erro')
def passo(context, nome):
    ids = {'data': 'data', 'valor': 'valor', 'descrição': 'descricao'}
    msg = context.browser.find_element_by_css_selector(
        '#' + ids[nome] + '.error')
    assert_that(msg, not_none())


@step('preencho o campo "{nome}" com "{valor}"')
def passo(context, nome, valor):
    ids = {'data': 'data', 'valor': 'valor', 'descrição': 'descricao'}
    elemento = context.browser.find_element_by_id(ids[nome])
    elemento.clear()
    elemento.send_keys(valor)


@step('devo ser direcionado à página de despesas')
def passo(context):
    url = context.browser.current_url
    assert_that(url, starts_with(context.url('/despesas')))
