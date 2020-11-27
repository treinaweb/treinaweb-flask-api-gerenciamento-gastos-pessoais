from api import db
import enum

class TipoEnum(enum.Enum):
    entrada = 1
    saida = 2

class Transacao(db.Model):
    __tablename__ = "transacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum(TipoEnum), nullable=False)
    conta_id = db.Column(db.Integer, db.ForeignKey("conta.id"))