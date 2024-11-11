from flask import Flask
from blueprints.webhook.pagamentos import pagamentos
from blueprints.cadastro.cadastro import cadastro
from blueprints.login.login import login
from blueprints.home.info_pagamentos.info_pagamentos import tratativas
from blueprints.home.informacoes.informacoes import informacoes
from classes.database.database import db
from config import Config


app = Flask(__name__)

# secret_key
app.secret_key = Config.SECRET_KEY

# conexão com DB por meio do SQLALchemy, coloquei aqui porque eu preciso passar o 'app' como parâmetro e não posso gerar 'cirule_import'.
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    return app

app.register_blueprint(pagamentos)
app.register_blueprint(cadastro)
app.register_blueprint(login)
app.register_blueprint(tratativas)
app.register_blueprint(informacoes)

app = create_app()
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True)
