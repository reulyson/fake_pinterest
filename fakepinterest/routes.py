from flask import Flask, render_template, url_for
from fakepinterest import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)