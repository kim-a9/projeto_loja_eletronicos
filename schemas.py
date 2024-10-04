from marshmallow import Schema, fields

class CadastroProdutoSchema(Schema):
    id = fields.Str(dump_only=True)
    codigoproduto = fields.Int(required=True)
    produto = fields.Str(required=True)
    categoria = fields.Str()
    quantidade = fields.Int(dump_only=True)

class EditarProdutoSchema(Schema):
    codigoproduto = fields.Int(required=True)
    produto = fields.Str(required=True)
    categoria = fields.Str()
    quantidade = fields.Int()

