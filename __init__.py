from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')
jwt = JWTManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
mi = Migrate(app, db)

api = Api(app)

from .models import conta_model, transacao_model, usuario_model
from .views import conta_view, transacao_view, usuario_view, login_view