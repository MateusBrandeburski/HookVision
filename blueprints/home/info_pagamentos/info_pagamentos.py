from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from classes.database.database import Pagamentos


tratativas = Blueprint('tratativas', __name__, template_folder='template')


# redenderiza tabela que mostra os dados no banco de dados.
@tratativas.route('/tratativas')
def index():
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))

    else:
        pagamentos = Pagamentos.query.all()

        # Converte os resultados em uma lista de dicionários
        dados = [{
                "nome": pagamento.nome,
                "email": pagamento.email,
                "status": pagamento.status,
                "status_no_sistema": pagamento.status_no_sistema,
                "valor": pagamento.valor,
                "forma_pagamento": pagamento.forma_pagamento,
                "parcelas": pagamento.parcelas,
                "data": pagamento.data
                  } for pagamento in pagamentos]

        return render_template('home/info_pagamentos/info_pagamentos.html', pagamentos=dados)



