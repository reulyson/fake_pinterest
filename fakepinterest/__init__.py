from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# criação aplicação
app = Flask(__name__)

# criação do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
 
# Importa partes do projeto
from fakepinterest import routes