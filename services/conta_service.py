from ..models import conta_model
from api import db

def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, descricao=conta.descricao, saldo=conta.saldo)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd

def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas

def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta