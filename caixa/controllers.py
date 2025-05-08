from datetime import datetime

# Função para registrar a venda
def registrar_venda(data):
    try:
        total = data['total']
        desconto = data['desconto']
        metodo_pagamento = data['metodo_pagamento']
        troco = data['troco']
        itens = data['itens']
        
        # Lógica de salvamento da venda no banco de dados ou processamento
        # Suponhamos que aqui registramos no banco ou fazemos alguma outra ação
        mensagem = f"Venda realizada com sucesso! Total: R$ {total} - Desconto: {desconto}%"
        
        return {"mensagem": mensagem, "status": "success"}
    except Exception as e:
        return {"mensagem": f"Erro ao registrar a venda: {str(e)}", "status": "error"}
