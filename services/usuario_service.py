from ..models import usuario_model
from api import db

def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha()
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db