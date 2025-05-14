from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# criação aplicação
app = Flask(__name__)

# configuração
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'b3170228513c507e5880372b8541ff2d'

# funconalidades
database = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
bcrypt = Bcrypt(app)
 
# Importa partes do projeto
from fakepinterest import routes