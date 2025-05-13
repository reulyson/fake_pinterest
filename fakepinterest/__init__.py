from flask import Flask

# criação aplicação
app = Flask(__name__)

# Importa partes do projeto
from fakepinterest import routes