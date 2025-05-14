# Cria o banco de dados do site
from fakepinterest import app, database, login_manager
from flask_login import UserMixin

# configuração de login
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    nome = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    foto = database.relationship('Foto', backref='usuario', lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    imagem = database.Column(database.String, default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default='datetime.utcnow')
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)