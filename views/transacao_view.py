from flask_restful import Resource
from api import api
from ..schemas import transacao_schema
from flask import request, make_response, jsonify
from ..entidades import transacao
from ..services import transacao_service, conta_service
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators import autorizacao_user

class TransacaoList(Resource):
    @jwt_required
    def get(self):
        usuario = get_jwt_identity()
        transacoes = transacao_service.listar_transacoes(usuario=usuario)
        cs = transacao_schema.TransacaoSchema(many=True)
        return make_response(cs.jsonify(transacoes), 200)

    @jwt_required
    def post(self):
        cs = transacao_schema.TransacaoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            valor = request.json["valor"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                transacao_nova = transacao.Transacao(nome=nome, descricao=descricao,
                                            valor=valor, tipo=tipo, conta=conta)
                result = transacao_service.cadastrar_transacao(transacao_nova)
                return make_response(cs.jsonify(result), 201)

class TransacaoDetail(Resource):
    @autorizacao_user.transacao_user
    def get(self, id):
        transacao = transacao_service.listar_transacao_id(id)
        cs = transacao_schema.TransacaoSchema()
        return make_response(cs.jsonify(transacao), 200)

    @autorizacao_user.transacao_user
    def put(self, id):
        transacao_bd = transacao_service.listar_transacao_id(id)
        cs = transacao_schema.TransacaoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            valor = request.json["valor"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                transacao_nova = transacao.Transacao(nome=nome, descricao=descricao,
                                            valor=valor, tipo=tipo, conta=conta)
                transacao_atualizada = transacao_service.editar_transacao(transacao_bd, transacao_nova)
                return make_response(cs.jsonify(transacao_atualizada), 200)

    @autorizacao_user.transacao_user
    def delete(self, id):
        transacao = transacao_service.listar_transacao_id(id)
        transacao_service.remover_transacao(transacao)
        return make_response('', 204)

api.add_resource(TransacaoList, '/transacoes')
api.add_resource(TransacaoDetail, '/transacoes/<int:id>')