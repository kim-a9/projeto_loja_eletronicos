from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    codigoprod = IntegerField('Código:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    categoria = StringField('Categoria:')
    quantidade = IntegerField('Quantidade:')
    submit = SubmitField('Cadastrar')

class EditarProdutoForm(FlaskForm):
    codigoprod = IntegerField('Código: ', render_kw={'readonly':True})
    produto = StringField('Produto: ', validators=[DataRequired()])
    categoria = StringField('Categoria: ')
    quantidade = IntegerField('Quantidade: ', validators={DataRequired()})
    submit = SubmitField('Editar')

class VendasForm(FlaskForm):
    codigo = IntegerField('Código da Venda:', validators=[DataRequired()])
    codigoprod = IntegerField('Código do  Produto:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    qtd = IntegerField('Quantidade:', validators=[DataRequired()])
    submit = SubmitField('Registrar Venda')
