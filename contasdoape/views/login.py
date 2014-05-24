from flask.ext.login import (login_user, logout_user, login_required,
                             current_user, AnonymousUserMixin)
from flask import g, render_template, request, redirect, url_for, session
from contasdoape.models import Condominio, Usuario, ControleDeAcesso
from contasdoape.autenticacao import FacebookProvider
from contasdoape.web import app, login_manager
from flask import session


@login_manager.user_loader
def load_user(userid):
    usuario = ControleDeAcesso().carregar_usuario(userid)
    g.usuario = usuario

    return usuario


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

    session['provider'] = provider.get_descriptor()
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
        provider = FacebookProvider.from_descriptor(session['provider'])

        return redirect(provider.logout(url_for('logout', _external=True)))
    except:
        return redirect('logout')


@app.route('/authorized')
def authorized():
    provider = FacebookProvider.from_descriptor(session['provider'])

    usuario = provider.logar(request.args)
    condominio = Condominio(usuario)

    login_user(usuario)

    if not condominio.tem_ape():
        if condominio.eh_convidado():
            return redirect(url_for('dividir_ape'))

        return redirect(url_for('criar_ape'))

    return redirect(url_for('index'))
