from flask import render_template, request, jsonify
from .controllers import registrar_venda

# Rota para exibir o registro de compras
@app.route('/caixa')
def caixa():
    return render_template('caixa.html')

# Rota para processar a venda
@app.route('/registrar-venda', methods=['POST'])
def registrar_venda_view():
    data = request.get_json()
    resposta = registrar_venda(data)
    return jsonify(resposta)
