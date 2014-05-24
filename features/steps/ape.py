from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from hamcrest import *
from behave import *


def esperar(driver, elemento, tempo):
    return WebDriverWait(driver, tempo).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))


@step('que eu estou na página de informações do apê')
def passo(context):
    context.browser.get(context.url('/ape'))


@step('eu clico no link de alterar o dia')
def passo(context):
    context.browser.find_element_by_css_selector('.dia-do-acerto > a').click()


@step('eu deixo o campo em branco')
def passo(context):
    esperar(context.browser, '#dia', 2).clear()


@step('eu preencho o campo com "{valor}"')
def passo(context, valor):
    campo = esperar(context.browser, '#dia', 2)
    campo.clear()
    campo.send_keys(valor)


@step('eu devo ver uma mensagem de erro')
def passo(context):
    assert_that(esperar(context.browser, '#dia + .error', 2), not_none())


@step('clico no botão "Salvar"')
def passo(context):
    esperar(context.browser, '#alterar_dia', 2).click()


@step('devo ver que dia do acerto agora é "{dia}"')
def passo(context, dia):
    el = esperar(context.browser, '.dia-do-acerto > p', 2)
    assert_that(str(dia), equal_to(el.text))
