from flask.ext.login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, session 
from contasdoape.web import app, login_manager

@app.route("/primeiroacesso")
@login_required
def primeiro_acesso():
    return render_template('primeiroacesso.html', usuario = current_user)

@app.route("/convidaramigos")
@login_required
def convidar_amigos():
    return render_template('convidaramigos.html', usuario = current_user)
