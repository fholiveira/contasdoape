from flask import render_template, request, redirect, url_for, session 
from flask.ext.login import login_user, logout_user, login_required, current_user
from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from contasdoape.models.Condominio import Condominio
from contasdoape.models.Usuario import Usuario
from contasdoape.views.providers import Facebook
from contasdoape.web import app, login_manager

@login_manager.user_loader
def load_user(userid):
    return ControleDeAcesso().carregar_usuario(userid)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    facebook = Facebook(url_for('authorized', _external = True))
    return redirect(facebook.login_url())

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/primeiroacesso")
@login_required
def primeiro_acesso():
    return render_template('primeiroacesso.html', usuario = current_user)

@app.route('/authorized')
def authorized():
    facebook = Facebook(url_for('authorized', _external = True))
    usuario = facebook.logar(request.args)

    login_user(usuario)

    if not Condominio().tem_ape(usuario):
        return redirect(url_for('primeiro_acesso'))

    return redirect(url_for('sumario'))
