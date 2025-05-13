from flask import Flask

# criação aplicação
app = Flask(__name__)

# rotas
@app.route('/')
def index():
    return 'FakePinterest - Meu primeiro site no ar'

# rodar projeto
if __name__ == '__main__':
    app.run(debug=True)