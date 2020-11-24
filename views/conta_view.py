from flask_restful import Resource
from ..schemas import conta_schema
from flask import request, make_response, jsonify
from ..entidades import conta
from ..services import conta_service
from api import api

class ContaList(Resource):
    def get(self):
        contas = conta_service.listar_contas()
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 200)

    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            saldo = request.json["saldo"]
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo)
            result = conta_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(result), 201)

class ContaDetail(Resource):
    pass

api.add_resource(ContaList, '/contas')