from flask import render_template, request, redirect, url_for, session 
from flask.ext.login import login_user, logout_user, login_required
from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from contasdoape.web import app, login_manager
from contasdoape.models.Usuario import Usuario
from contasdoape.views.providers import Facebook

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

@app.route('/authorized')
def authorized():
    facebook = Facebook(url_for('authorized', _external = True))
    usuario = facebook.logar(request.args)

    if not usuario:
        return redirect(url_for('index'))

    login_user(usuario)
    return redirect(url_for('sumario'))
