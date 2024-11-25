from flask import Flask, session
from flask_babel import Babel, _
from routes.webhook.pagamentos import pagamentos
from routes.cadastro.cadastro import cadastro
from routes.login.login import login
from routes.langs.langs import langs
from routes.home.tabela.tabela import tratativas
from routes.home.cards.cards import cards
from classes.database.database import db
from datetime import timedelta
from config import Config


app = Flask(__name__, template_folder='views')

# secret_key
app.secret_key = Config.SECRET_KEY
app.permanent_session_lifetime = timedelta(minutes=1440)


# Configuração do Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Idioma padrão
app.config['BABEL_SUPPORTED_LOCALES'] = ['pt_BR', 'en']  # Idiomas suportados

babel = Babel(app)

def get_locale():
    return session.get('lang', 'en')

babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(pagamentos)
app.register_blueprint(cadastro)
app.register_blueprint(langs)
app.register_blueprint(login)
app.register_blueprint(tratativas)
app.register_blueprint(cards)


def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    return app


app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
