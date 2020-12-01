from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service

class UsuarioList(Resource):
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
            result = usuario_service.cadastrar_usuario(usuario_novo)
            return make_response(us.jsonify(result), 201)

api.add_resource(UsuarioList, '/usuarios')