from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.database.database import db, Pagamentos

tratativas = Blueprint('tratativas', __name__, template_folder='template')

# redenderiza tabela que mostra os dados no banco de dados.
@tratativas.route('/tratativas')
def index():
    
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:      
        pagamentos = Pagamentos.query.all()
        return render_template('home/info_pagamentos/info_pagamentos.html', pagamentos=pagamentos)
    

@tratativas.route('/filtro-por-email', methods=['GET','POST'])
def status_completo():
    
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:   
        email_filtrado = request.form.get('email')
        filtros = Pagamentos.query.filter_by(email=email_filtrado).all()
        if filtros:
            return render_template('home/info_pagamentos/info_pagamentos.html', filtros=filtros)
        else:
            flash('Email não encontrado na base de dados!')
            return render_template('home/info_pagamentos/info_pagamentos.html', filtros=filtros)