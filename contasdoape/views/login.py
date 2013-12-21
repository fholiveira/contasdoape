from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from contasdoape.models.UsuarioRepository import UsuarioRepository
from contasdoape import app, login_manager, facebook
from contasdoape.models.Usuario import Usuario

@login_manager.user_loader
def load_user(userid):
    return UsuarioRepository.carregar(userid)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    params = {'redirect_uri': redirect_uri}
    return redirect(facebook.get_authorize_url(**params))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/authorized')
def authorized():
    # check to make sure the user authorized the request
    if not 'code' in request.args:
        return redirect(url_for('index'))

    # make a request for the access token credentials using code
    redirect_uri = url_for('authorized', _external=True)
    data = dict(code=request.args['code'], redirect_uri=redirect_uri)

    session = facebook.get_auth_session(data=data)
    me = session.get('me').json()

    usuario = UsuarioRepository().carregar_ou_criar(me['username'], me['id'])
    print(usuario.nome)
    login_user(usuario)

    return redirect(url_for('sumario'))
