from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(db_url=None):  
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin123'
    app.config["API_TITLE"] = "Estokey REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite3:///projeto_loja_eletronicos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE EXCEPTIONS'] = True
    api = Api(app)
    db = SQLAlchemy()
    migrate = Migrate(app, db)
     

    # db.init_app(app)
    migrate.init_app(app, db)

    # with app.app_context():
    #     from .models import CadastroProduto
    #     db.create_all()


    from routes import bp
    app.register_blueprint(bp)

    if __name__ == '__main__':
        api.run(debug=True)

     
    return app
