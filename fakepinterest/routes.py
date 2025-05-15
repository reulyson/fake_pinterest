from flask import Flask, render_template, redirect, url_for
from fakepinterest import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormCriarConta, FormLogin
from fakepinterest.models import Usuario

@app.route('/', methods=['GET', 'POST'])
def index():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        username = Usuario.query.filter_by(email=form_login.usuario.data).first()
        if username and bcrypt.check_password_hash(username.senha, form_login.senha.data):
            login_user(username)
            return redirect(url_for('perfil', id_usuario=username.id))
           
    return render_template('index.html', form=form_login)

@app.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    form_criar_conta = FormCriarConta()

    # Pega os dados do formulário
    if form_criar_conta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(
            username=form_criar_conta.username.data,
            senha=senha, 
            email=form_criar_conta.email.data
            )
        
        # Envia os dados para o banco
        database.session.add(usuario)
        database.session.commit()

        # realiza o login após cadastro
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criar_conta.html', form=form_criar_conta)

@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    # se o usuário estiver no próprio perfil
    if int(id_usuario) == int(current_user.id):
        return render_template('perfil.html', usuario=current_user)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))