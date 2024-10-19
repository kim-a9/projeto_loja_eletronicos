from db import db


class CadastroProduto(db.Model):
    __tablename__ = 'cadastro_produto'

    id = db.Column(db.Integer, primary_key=True)
    codigoprod = db.Column(db.Integer, nullable=False, unique=True)
    produto = db.Column(db.String(100), nullable=False)
    categoria  = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)

