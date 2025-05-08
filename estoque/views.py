from flask import render_template

@estoque_bp.route('/')
def estoque_home():
    return render_template('estoque.html')
from flask import render_template, request, jsonify
from .models import Produto
from .controllers import cadastrar_produto, listar_produtos

# Rota para exibir o cadastro de produtos
@app.route('/estoque/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto_view():
    if request.method == 'POST':
        dados_produto = request.form
        produto = cadastrar_produto(dados_produto)
        return jsonify(produto)
    return render_template('estoque/cadastrar.html')

# Rota para listar os produtos no estoque
@app.route('/estoque/produtos', methods=['GET'])
def listar_produtos_view():
    produtos = listar_produtos()
    return jsonify(produtos)
