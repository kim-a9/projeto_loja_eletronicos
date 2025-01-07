from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import * 
import psycopg2
import os

# import logging 

# basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


# db_url=None


def create_app():  
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin123'
    app.config["API_TITLE"] = "Estokey"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "2.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["CSRF_ENABLED"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@localhost:5432/projeto_estokey"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['PDF_FOLDER'] = 'static/pdf/'
    app.config['TEMPLATE_FOLDER'] = 'templates/relatorio'

    db_params = {
        'dbname': 'projeto_estokey',
        'user': 'postgres',
        'password': '1234',
        'host': 'localhost',
        'port': '5432'
    }
    try:
        # Estabelece a conexão
        connection = psycopg2.connect(**db_params)
        if connection:
            print("Conexão estabelecida com sucesso!")
    except psycopg2.Error as error:
        print("Erro ao conectar ao PostgreSQL:", error)

    api = Api(app)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from routes import bp
    app.register_blueprint(bp)




    return app
