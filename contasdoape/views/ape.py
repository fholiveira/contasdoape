from flask.ext.login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, session
from contasdoape.web import app, login_manager
from contasdoape.models.Condominio import Condominio
from contasdoape.models.ControleDeAcesso import ControleDeAcesso

@app.route("/primeiroacesso")
@login_required
def primeiro_acesso():
    return render_template('primeiroacesso.html', usuario = current_user)

@app.route("/convidaramigos")
@login_required
def convidar_amigos():
    condominio = Condominio()
    usuario = ControleDeAcesso().carregar_usuario(current_user.facebook_id)
    print(usuario.id)
    if not condominio.tem_ape(usuario):
        condominio.criar_ape(usuario)

    return render_template('convidaramigos.html', usuario = current_user)

@app.route('/salvaramigos', methods=['POST'])
@login_required
def salvar_amigos():
    ids = [amigo['value'] for amigo in request.json]
    
    if not ids:
        return 'Ok', 200
   
    ape = Condominio().obter_ape(current_user)
    ape.adicionar_convidados(ids)

    return 'Ok', 200
