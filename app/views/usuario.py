from bottle import TEMPLATE_PATH, get, post, redirect, request, jinja2_template as template

@get('/usuario')
def mostrar_usuario():
    return template('usuario.html')

