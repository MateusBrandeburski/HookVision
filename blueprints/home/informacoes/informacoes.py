from flask import Blueprint, render_template, redirect, url_for, session, flash, jsonify
from classes.graficos.graficos import Graficos


informacoes = Blueprint('informacoes', __name__, template_folder='template')


# redenderiza tabela que mostra os dados no banco de dados.
@informacoes.route('/informacoes')
def index():
    if not session.get('usuario_logado', None):
        return redirect(url_for('login.index'))
    return render_template('home/informacoes/informacoes.html')
    

@informacoes.route('/grafico-status')
def grafico_status():
    if not session.get('usuario_logado', None):
        return "Session expided - 419", 419
    return jsonify(Graficos.grafico_status())

@informacoes.route('/grafico-total')
def grafico_total():
    if not session.get('usuario_logado', None):
        return "Session expided - 419", 419
    return jsonify(Graficos.grafico_total())

    