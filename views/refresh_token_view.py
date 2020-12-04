from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token, create_refresh_token
from api import api

class RefreshTokenList(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)
        return make_response(jsonify({
            'acess_token': access_token,
            'refresh_token': refresh_token
        }), 200)

api.add_resource(RefreshTokenList, '/token/refresh')