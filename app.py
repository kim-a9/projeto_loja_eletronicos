from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# import logging
import psycopg2
import os

basedir = os.path.abspath(os.path.dirname(__file__))



db = SQLAlchemy()

def init_db():
        conexao = psycopg2.connect(database = 'estokey',
                                host = 'localhost',
                                user = 'postgres', 
                                password = '1234',
                                port = '5432', encoding='utf-8')
        # cur = conexao.cursor()

        print(conexao.info)
        print(conexao.status)
        return conexao

def create_app(db_url=None):  
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin123'
    app.config["API_TITLE"] = "Estokey"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "2.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://' + os.path.join(basedir, 'db', 'estokey.db')
    app.config["CSRF_ENABLED"] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@localhost:5432/estokey, encoding='utf8' "
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    api = Api(app)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from routes import bp
    app.register_blueprint(bp)




    return app
