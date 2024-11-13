from flask import Blueprint, render_template, redirect, url_for, session, flash, jsonify
from classes.database.database import Pagamentos


informacoes = Blueprint('informacoes', __name__, template_folder='template')


# redenderiza tabela que mostra os dados no banco de dados.
@informacoes.route('/informacoes')
def index():
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))

    else:
        return render_template('home/informacoes/informacoes.html')
    


@informacoes.route('/grafico-status')
def grafico_status():
 
        reembolsado = Pagamentos.query.filter_by(status="reembolsado").count()
        aprovado = Pagamentos.query.filter_by(status="aprovado").count()
        recusado = Pagamentos.query.filter_by(status="recusado").count()
        # Formato do retorno
        resultado = {
            "reembolsado": reembolsado,
            "aprovado": aprovado,
            "recusado": recusado
        }

        return jsonify(resultado)

    