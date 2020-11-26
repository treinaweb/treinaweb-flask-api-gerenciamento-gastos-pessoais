from api import ma
from ..models import transacao_model
from marshmallow import fields


class TransacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = transacao_model.Transacao
        load_instance = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    valor = fields.Float(required=True)
    tipo = fields.String(required=True)
