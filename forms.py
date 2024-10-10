from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    codigoprod = IntegerField('Código:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    categoria = StringField('Categoria:', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade:')
    submit = SubmitField('Cadastrar')

class EditarProdutoForm(FlaskForm):
    editar_codigoprod = IntegerField('Código', validators=[DataRequired()])
    editar_produto = StringField('Produto: ', validators=[DataRequired()])
    editar_categoria = StringField('Categoria: ',  validators=[DataRequired()])
    editar_quantidade = IntegerField('Quantidade: ', validators={DataRequired()})
    submit = SubmitField('Editar')

class VendasForm(FlaskForm):
    codigo = IntegerField('Código da Venda:', validators=[DataRequired()])
    codigoprod = IntegerField('Código do  Produto:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    qtd = IntegerField('Quantidade:', validators=[DataRequired()])
    submit = SubmitField('Registrar Venda')



