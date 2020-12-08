from flask_restful import Resource
from ..schemas import conta_schema
from flask import request, make_response, jsonify
from ..entidades import conta
from ..services import conta_service, usuario_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators import autorizacao_user

class ContaList(Resource):
    @jwt_required
    def get(self):
        usuario = get_jwt_identity()
        contas = conta_service.listar_contas(usuario=usuario)
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 200)

    @jwt_required
    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            saldo = request.json["saldo"]
            usuario = get_jwt_identity()
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo, usuario=usuario)
            result = conta_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(result), 201)


class ContaDetail(Resource):
    @autorizacao_user.conta_user
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)

    @autorizacao_user.conta_user
    def put(self, id):
        conta_bd = conta_service.listar_conta_id(id)
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            saldo = request.json["saldo"]
            usuario = get_jwt_identity()
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo, usuario=usuario)
            result = conta_service.editar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(result), 201)

    @autorizacao_user.conta_user
    def delete(self, id):
        conta = conta_service.listar_conta_id(id)
        conta_service.remover_conta(conta)
        return make_response('', 204)


api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')