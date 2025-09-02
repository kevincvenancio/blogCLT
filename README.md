

Um sistema de blog com autenticação de usuários, posts e gerenciamento de perfis.  
Desenvolvido em **Flask** com deploy no **Railway**.

🔗 **Deploy Online**: [BlogCLT](https://blogclt-production.up.railway.app/)

---

## 🚀 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)  
- [Flask-WTF](https://flask-wtf.readthedocs.io/)  
- [Flask-Login](https://flask-login.readthedocs.io/)  
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/)  
- [Pillow](https://pillow.readthedocs.io/) (tratamento de imagens de perfil)  
- [Gunicorn](https://gunicorn.org/) (produção)  
- [PostgreSQL](https://www.postgresql.org/) (produção no Railway) / SQLite (desenvolvimento)

---

## 📖 Funcionalidades

- 👤 **Sistema de usuários**: cadastro, login, logout, edição de perfil.  
- 🖼️ **Foto de perfil** com upload e redimensionamento automático.  
- 📝 **Posts**: criar, visualizar, editar e excluir.  
- 🗂️ **Listagem de usuários** (apenas logado).  
- 📬 **Formulário de contato** com validação.  
- 🔒 **Autenticação** protegendo rotas sensíveis.  

---

## ⚙️ Instalação e Execução Local

### 1. Clone o repositório
```bash
git clone https://github.com/kevincvenancio/blogCLT.git
cd blogCLT
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto (ou exporte no terminal):

```env
SECRET_KEY=sua_chave_segura
DATABASE_URL=sqlite:///comunidade.db  # ou URL do PostgreSQL no Railway
```

### 5. Execute a aplicação
```bash
flask run
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deploy na Railway

O projeto está configurado para rodar no **Railway** usando:  
- `DATABASE_URL` → PostgreSQL gerenciado.  
- `gunicorn` → servidor de produção.  

Passos básicos para deploy:
1. Criar projeto no Railway.  
2. Adicionar banco PostgreSQL.  
3. Definir variáveis de ambiente (`DATABASE_URL`, `SECRET_KEY`).  
4. Fazer o deploy a partir do GitHub.  

---

## 📂 Estrutura do Projeto

```
blogCLT/
│── comunidadeimpressionadora/
│   ├── __init__.py        # Configuração da aplicação Flask
│   ├── models.py          # Modelos do banco de dados (Usuario, Post)
│   ├── forms.py           # Formulários (WTForms)
│   ├── routes.py          # Rotas da aplicação
│   ├── static/            # Arquivos estáticos (imagens, CSS, JS)
│   └── templates/         # Templates HTML (Jinja2)
│
├── requirements.txt       # Dependências do projeto
├── Procfile (opcional)    # Para deploy no Railway/Heroku
└── README.md              # Este arquivo
```
---

👨‍💻 Desenvolvido por [**Kevin Venancio**](https://github.com/kevincvenancio)

