from flask.ext.login import (login_user, logout_user, login_required,
                             current_user)
from flask import g, render_template, request, redirect, url_for, session
from contasdoape.autenticacao import FacebookProvider
from contasdoape.models import Condominio, Porteiro
from contasdoape.web import app, login_manager


@login_manager.user_loader
def load_user(userid):
    g.usuario = Porteiro.carregar_usuario(userid)
    return g.usuario


@app.route('/')
def index():
    if current_user.get_id():
        return redirect(url_for('listar_despesas'))

    return render_template('home.jinja')


@app.errorhandler(401)
@app.errorhandler(403)
def nao_autorizado(exception):
    return redirect(url_for('index'))


@app.route('/login')
def login():
    provider = FacebookProvider(url_for('authorized', _external=True),
                                app.config['FB_CLIENT_ID'],
                                app.config['FB_CLIENT_SECRET'])

    return redirect(provider.login_url())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/logoutall')
def logout_all():
    if not current_user or not app.config.get('DEBUG'):
        redirect(url_for('logout'))

    provider = FacebookProvider.from_descriptor(session['provider'])
    url = provider.logout_url(url_for('logout', _external=True))
    return redirect(url)


@app.route('/authorized')
def authorized():
    provider = FacebookProvider(url_for('authorized', _external=True),
                                app.config['FB_CLIENT_ID'],
                                app.config['FB_CLIENT_SECRET'])

    usuario = provider.logar(request.args)
    session['provider'] = provider.get_descriptor()

    condominio = Condominio(usuario)
    cracha = Porteiro(usuario)

    login_user(usuario)

    if not cracha.tem_ape():
        if cracha.eh_convidado():
            return redirect(url_for('dividir_ape'))

        return redirect(url_for('criar_ape'))

    return redirect(url_for('index'))
