from flask import render_template, request, redirect, url_for, flash
from contasdoape.models.Usuario import Usuario
from contasdoape.models.UsuarioRepository import UsuarioRepository
from contasdoape import app, facebook
from contasdoape.models.Usuario import Usuario
from contasdoape.models.UsuarioRepository import UsuarioRepository

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/facebook/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    params = {'redirect_uri': redirect_uri}
    return redirect(facebook.get_authorize_url(**params))


@app.route('/facebook/authorized')
def authorized():
    # check to make sure the user authorized the request
    if not 'code' in request.args:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    # make a request for the access token credentials using code
    redirect_uri = url_for('authorized', _external=True)
    data = dict(code=request.args['code'], redirect_uri=redirect_uri)

    session = facebook.get_auth_session(data=data)

    # the "me" response
    me = session.get('me').json()

    UsuarioRepository().carregar_ou_criar(me['username'], me['id'])

    flash('Logged in as ' + me['name'])
    return redirect(url_for('sumario'))
