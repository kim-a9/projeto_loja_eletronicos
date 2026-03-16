from app import db

class CadastroProduto(db.Model):
    __tablename__ = 'cadastro_produto'

    id = db.Column(db.Integer, primary_key=True)
    codigoprod = db.Column(db.Integer, nullable=False, unique=True, index=True)
    produto = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)

    @classmethod
    def find_by_cod(cls, codigoprod):
        return cls.query.filter_by(codigoprod=codigoprod).first()
    
    def __repr__(self):
        return f"CadastroProduto('{self.codigoprod}', '{self.produto}', '{self.quantidade}')"