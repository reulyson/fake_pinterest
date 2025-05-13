from flask import Flask, render_template, url_for

# criação aplicação
app = Flask(__name__)

# rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

# rodar projeto
if __name__ == '__main__':
    app.run(debug=True)