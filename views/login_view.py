from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services.usuario_service import listar_usuario_email
from flask_jwt_extended import create_access_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        email = request.json["email"]
        senha = request.json["senha"]
        usuario_bd = listar_usuario_email(email)
        if usuario_bd and usuario_bd.ver_senha(senha):
            access_token = create_access_token(
                identity=usuario_bd.id,
                expires_delta=timedelta(seconds=200)
            )
            return make_response(jsonify({
                'acess_token': access_token,
                'message': 'login realizado com sucesso'
            }), 200)
        return make_response(jsonify({
            'message': 'Credenciais inválidas'
        }), 401)

api.add_resource(LoginList, '/login')

