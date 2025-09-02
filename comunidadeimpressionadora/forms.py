from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField("Confirmação da Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail, ou faça login para continuar")



class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")


class FormEditarPerfil(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField("Atualizar foto de perfil", validators=[FileAllowed(["jpg", "png"])])
    curso_excel = BooleanField("Empresário")
    curso_vba = BooleanField("Engenheiro")
    curso_powerbi = BooleanField("Pedreiro")
    curso_python = BooleanField("Dentista")
    curso_ppt = BooleanField("Vendedor")
    curso_sql = BooleanField("Programador")
    botao_submit_editarperfil = SubmitField("Confirmar Edição")

def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com esse e-mail> Cadastre outro e-mail")
            

class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField("Criar Post")


class ContactForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Mensagem", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Enviar")



