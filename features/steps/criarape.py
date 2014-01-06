from behave import *

@step('clicar no botão "Vou criar o apê agora mesmo"')
def passo(context):
    context.browser.find_element_by_id('criar_ape').click()
    
@step('eu devo ser redirecionado a página de convidar amigos')
def passo(context):
    url = context.browser.current_url 
    assert url.startswith(context.url('/convidaramigos'))
