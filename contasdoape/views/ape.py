from flask.ext.login import login_required, current_user
from flask import render_template, request, redirect, url_for
from contasdoape.models import Condominio, Porteiro
from contasdoape.web import app


@app.route("/criar-ape")
@login_required
def criar_ape():
    if Porteiro(current_user).tem_ape():
        redirect(url_for('index'))

    return render_template('criar-ape.jinja')


@app.route("/ape")
@login_required
def ape():
    apto = Condominio(current_user).obter_ape()
    return render_template('ape.jinja', ape=apto)


@app.route("/ape/mudar-dia-do-acerto", methods=['POST'])
@login_required
def mudar_dia_do_acerto():
    apto = Condominio(current_user).obter_ape()

    dia = request.form['dia'] or apto.dia_do_acerto
    apto.dia_do_acerto = dia
    apto.save()

    return 'Ok', 200


@app.route("/dividir-ape")
@login_required
def dividir_ape():
    porteiro = Porteiro(current_user)

    if porteiro.tem_ape() or not porteiro.eh_convidado():
        redirect(url_for('index'))

    apto = Condominio(current_user).obter_ape()

    return render_template('dividir-ape.jinja', usuarios=list(apto.membros))


@app.route("/aceitar-convite", methods=['POST'])
@login_required
def aceitar_convite():
    cracha = Porteiro(usuario)

    if not cracha.tem_ape() and cracha.eh_convidado():
        Condominio(usuario).aceitar_convite()

    return redirect(url_for('index'))


@app.route("/convidar-amigos")
@login_required
def convidar_amigos():
    if not Porteiro(current_user).tem_ape():
        usuario = Porteiro.carregar_usuario(current_user.facebook_id)
        Condominio(usuario).criar_ape()

    return render_template('convidar-amigos.jinja')


@app.route('/salvar-amigos', methods=['POST'])
@login_required
def salvar_amigos():
    ids = [amigo['value'] for amigo in request.json]

    if not ids:
        return 'Ok', 200

    usuario = Porteiro.carregar_usuario(current_user.facebook_id)
    Condominio(usuario).incluir_convidados(ids)

    return 'Ok', 200
