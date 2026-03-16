from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import create_engine
import os


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):  
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    from routes import bp as main_bp
    app.register_blueprint(main_bp)

    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        with engine.connect() as conn:
            print("Conexão estabelecida com sucesso!")
    except Exception as error:
        print("Erro ao conectar ao PostgreSQL:", error)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

