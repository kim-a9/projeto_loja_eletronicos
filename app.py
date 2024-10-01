from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# from models import CadastroProduto
# from . import db

# db = SQLAlchemy(app)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'admin123'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projeto_loja_eletronicos.db'


    






if __name__ == '__main__':
    app.run(debug=True)
