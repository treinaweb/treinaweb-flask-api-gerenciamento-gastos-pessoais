from api import ma
from ..models import conta_model
from marshmallow import fields
from ..schemas import transacao_schema

class ContaSchema(ma.SQLAlchemyAutoSchema):
    transacoes = ma.Nested(transacao_schema.TransacaoSchema, many=True)
    class Meta:
        model = conta_model.Conta
        load_instance = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    saldo = fields.Float(required=True)
    usuario_id = fields.Integer(required=True)
