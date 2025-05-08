from flask import render_template, jsonify
from .controllers import listar_produtos, adicionar_ao_carrinho

# Rota para o catálogo de produtos
@app.route('/catalogo')
def catalogo():
    produtos = listar_produtos()
    return render_template('catalogo.html', produtos=produtos)

# Rota para adicionar produtos ao carrinho
@app.route('/adicionar-carrinho', methods=['POST'])
def adicionar_carrinho_view():
    dados = request.get_json()
    adicionar_ao_carrinho(dados)
    return jsonify({"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"})
