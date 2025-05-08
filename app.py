from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação
app = Flask(__name__)

# Configurações do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supermercado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Modelo de exemplo: Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Produto {self.nome}>'

# Função para criar o banco de dados e tabelas
def create_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados criado com sucesso!")

# Rota de teste
@app.route('/')
def home():
    return "Bem-vindo ao sistema de gestão de supermercado!"

# Executa a aplicação
if __name__ == '__main__':
    create_db()
    app.run(debug=True, port=5001)

