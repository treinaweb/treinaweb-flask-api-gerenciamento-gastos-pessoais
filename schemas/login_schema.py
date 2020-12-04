from api import ma
from ..models import usuario_model
from marshmallow import fields

class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario

    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)