from functools import wraps

from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..services import conta_service, transacao_service
from flask import make_response, jsonify

def conta_user(view_function):
    @wraps(view_function)
    def decorator_function(*args, **kwargs):
        verify_jwt_in_request()
        usuario = get_jwt_identity()
        conta = conta_service.listar_conta_id(kwargs['id'])
        if conta is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        elif conta.usuario_id == usuario:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify("Esta conta não pertence ao usuário logado"), 403)
    return decorator_function

def transacao_user(view_function):
    @wraps(view_function)
    def decorator_function(*args, **kwargs):
        verify_jwt_in_request()
        usuario = get_jwt_identity()
        transacao = transacao_service.listar_transacao_id(kwargs['id'])
        if transacao is None:
            return make_response(jsonify("Transação não encontrada"), 404)
        else:
            conta = conta_service.listar_conta_id(transacao.conta_id)
            if conta.usuario_id == usuario:
                return view_function(*args, **kwargs)
            else:
                return make_response(jsonify("Esta transação não pertence ao usuário logado"), 403)
    return decorator_function