from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request
from classes.dashboard.tabela import Tabela

tratativas = Blueprint('tratativas', __name__, template_folder='template')


#--entender o ciclo do software e por que ele recebeu o nome de tratativas? ----#
@tratativas.route('/tratativas')
def index():
    if not session.get('usuario_logado', None):
        return redirect(url_for('login.index'))
    return render_template('home/dashboard/dashboard.html')
#------------------------------------------------------------------#


# @tratativas.route('/table')
# def table():
#     if not session.get('usuario_logado', None):
#         return "Session expided - 419", 419
    
#     limit = int(request.args.get('limit', 10))
#     offset = int(request.args.get('offset', 0))
#     return jsonify(Tabela.tabela_paginada(limit=limit, offset=offset))


@tratativas.route('/table')
def table_autocomplite():
    if not session.get('usuario_logado', None):
        return "Session expided - 419", 419
    
    search = request.args.get('search')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    return jsonify(Tabela.search_auto_complite(search_term=search, limit=limit, offset=offset))