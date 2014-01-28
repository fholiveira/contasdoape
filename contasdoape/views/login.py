from flask.ext.login import (login_user, logout_user, login_required, 
                             current_user, AnonymousUserMixin)
from flask import render_template, request, redirect, url_for, session 
from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from contasdoape.models.Condominio import Condominio
from contasdoape.views.providers import Facebook
from contasdoape.models.Usuario import Usuario
from contasdoape.web import app, login_manager

@login_manager.user_loader
def load_user(userid):
    return ControleDeAcesso().carregar_usuario(userid)

@app.route('/')
def index():
    if current_user.is_anonymous:
        return render_template('home.html')

    return redirect(url_for('listar_despesas')) 

@app.route('/login')
def login():
    provider = Facebook(url_for('authorized', _external = True))
    return redirect(provider.login_url())

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/logoutall')
def logout_all():
    if not app.config.get('DEBUG'):
        redirect(url_for('logout'))

    try:
        provider = Facebook(url_for('authorized', _external = True))
        return redirect(provider.logout(url_for('index', _external=True)))
    except:
        return redirect('/')

@app.route('/authorized')
def authorized():
    provider = Facebook(url_for('authorized', _external = True))
    usuario = provider.logar(request.args)
    
    login_user(usuario)

    if not Condominio().tem_ape(usuario):
        return redirect(url_for('primeiro_acesso'))

    return redirect(url_for('sumario'))
