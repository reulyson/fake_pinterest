from flask import Flask, render_template

# criação aplicação
app = Flask(__name__)

# rotas
@app.route('/')
def index():
    return render_template('index.html')

# rodar projeto
if __name__ == '__main__':
    app.run(debug=True)