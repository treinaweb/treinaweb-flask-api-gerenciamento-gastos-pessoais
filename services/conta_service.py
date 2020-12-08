from ..models import conta_model
from api import db

def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, descricao=conta.descricao, saldo=conta.saldo,
                                 usuario_id=conta.usuario)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd

def listar_contas(usuario):
    contas = conta_model.Conta.query.filter_by(usuario_id=usuario).all()
    return contas

def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta

def remover_conta(conta):
    db.session.delete(conta)
    db.session.commit()

def editar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.descricao = conta_nova.descricao
    conta.saldo = conta_nova.saldo
    db.session.commit()
    return conta

def alterar_saldo_conta(id_conta, transacao, tipo_operacao, valor_antigo=None):
    ## 1: Cadastro
    ## 2: Edicao
    ## 3: Remocao
    conta = listar_conta_id(id_conta)
    if tipo_operacao == 1:
        if transacao.tipo == "1":
            conta.saldo += transacao.valor
        else:
            conta.saldo -= transacao.valor
    elif tipo_operacao == 2:
        if transacao.tipo == "1":
            conta.saldo -= valor_antigo
            conta.saldo += transacao.valor
        else:
            conta.saldo += valor_antigo
            conta.saldo -= transacao.valor
    else:
        if transacao.tipo.value == 1:
            conta.saldo -= transacao.valor
        else:
            conta.saldo += transacao.valor
    db.session.commit()