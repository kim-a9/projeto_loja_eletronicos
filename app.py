from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api

import routes

# from models import CadastroProduto
# from . import dbs

db = SQLAlchemy()

def create_app(db_url=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin123'
    app.config['PROPAGATE EXCEPTIONS'] = True
    app.config["API_TITLE"] = "Estokey REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projeto_loja_eletronicos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()


    from routes import bp
    app.register_blueprint(bp)

    if __name__ == '__main__':
        app.run(debug=True)
     
    return app
