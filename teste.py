from fakepinterest import app, database
from fakepinterest.models import Foto, Usuario

id = 1

# Crie um contexto de aplicação
with app.app_context():
    usuario = Usuario.query.get(int(id))
    for foto in usuario.foto:
        print(foto.imagem)