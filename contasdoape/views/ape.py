from flask.ext.login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, session
from contasdoape.web import app, login_manager
from contasdoape.models.Condominio import Condominio
from contasdoape.models.ControleDeAcesso import ControleDeAcesso


@app.route("/criar-ape")
@login_required
def criar_ape():
    if Condominio(current_user).tem_ape():
        redirect(url_for('index'))

    return render_template('criar-ape.jinja')


@app.route("/ape")
@login_required
def ape():
    ape = Condominio(current_user).obter_ape()
    return render_template('ape.jinja', ape=ape)


@app.route("/dividir-ape")
@login_required
def dividir_ape():
    condominio = Condominio(current_user)

    if condominio.tem_ape() or not condominio.eh_convidado():
        redirect(url_for('index'))

    ape = condominio.obter_ape()

    return render_template('dividir-ape.jinja', usuarios=list(ape.membros))


@app.route("/aceitar-convite", methods=['POST'])
@login_required
def aceitar_convite():
    condominio = Condominio(current_user)

    if not condominio.tem_ape() and condominio.eh_convidado():
        condominio.aceitar_convite()

    return redirect(url_for('index'))


@app.route("/convidar-amigos")
@login_required
def convidar_amigos():
    usuario = ControleDeAcesso().carregar_usuario(current_user.facebook_id)
    condominio = Condominio(usuario)

    if not condominio.tem_ape():
        condominio.criar_ape()

    return render_template('convidar-amigos.jinja')


@app.route('/salvar-amigos', methods=['POST'])
@login_required
def salvar_amigos():
    ids = [amigo['value'] for amigo in request.json]

    if not ids:
        return 'Ok', 200

    ape = Condominio(current_user).obter_ape()
    ape.adicionar_convidados(ids)

    return 'Ok', 200
