from ..models import usuario_model
from api import db

def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha()
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()

def listar_usuario_id(id):
    return usuario_model.Usuario.query.filter_by(id=id).first()