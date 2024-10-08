from marshmallow import Schema, fields

class CadastroProdutoSchema(Schema):
    id = fields.Str(dump_only=True)
    codigoproduto = fields.Int(required=True)
    produto = fields.Str(required=True)
    categoria = fields.Str()
    quantidade = fields.Int(dump_only=True)

class EditarProdutoSchema(Schema):
    editar_codigoprod = fields.Int(required=True)
    editar_produto = fields.Str(required=True)
    editar_categoria = fields.Str()
    editar_quantidade = fields.Int()

