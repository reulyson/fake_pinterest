# Cria os formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    usuario = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao = SubmitField('Fazer login')

class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmar_senha = PasswordField('Confirmar senha', validators=[DataRequired(), ValidationError(), EqualTo('senha')])
    botao_confirmar =   SubmitField('Criar usuário')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() # Filtra o email na tabela usuario e pega o primeiro resultado
        if usuario:
            return ValidationError('E-mail existente, faça o logi para contiuar!')