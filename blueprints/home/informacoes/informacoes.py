from flask import Blueprint, render_template, redirect, url_for, session, flash, jsonify


informacoes = Blueprint('informacoes', __name__, template_folder='template')


# redenderiza tabela que mostra os dados no banco de dados.
@informacoes.route('/informacoes')
def index():
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))

    else:
        return render_template('home/informacoes/informacoes.html')