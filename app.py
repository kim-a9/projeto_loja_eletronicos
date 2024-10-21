from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))



db = SQLAlchemy()

def create_app(db_url=None):  
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin123'
    app.config["API_TITLE"] = "Estokey REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db', 'projeto_loja_eletronicos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    api = Api(app)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from routes import bp
    app.register_blueprint(bp)

    return app
