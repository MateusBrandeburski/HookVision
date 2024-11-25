# from flask import request, session, render_template

# def auth_middleware(app):
#     @app.before_request
#     def check_user_authentication():
#         # nos [] são o nome da route/blueprint e o nome da função que não precisa autenticação.
#         if request.endpoint in ['cadastro.register']:
#             return 

#         if 'usuario_logado' not in session or session['usuario_logado'] is None:
#             language = session.get('lang', 'en')
#             return render_template('login/form_login.html', lang=language)
