import os

class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY') or "loja_eletronicos_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"postgresql+psycopg2://postgres:1234@localhost:5432/projeto_estokey"

    API_TITLE = "Projeto Loja Eletrônicos"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"