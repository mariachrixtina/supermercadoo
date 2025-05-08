# Controllers podem ser mais complexos conforme os requisitos do método de pagamento
def processar_pagamento(metodo, valor):
    try:
        if metodo == 'dinheiro':
            return {"status": "sucesso", "mensagem": "Pagamento em dinheiro processado."}
        elif metodo == 'cartao':
            return {"status": "sucesso", "mensagem": "Pagamento com cartão processado."}
        elif metodo == 'pix':
            return {"status": "sucesso", "mensagem": "Pagamento via PIX processado."}
        else:
            return {"status": "erro", "mensagem": "Método de pagamento inválido."}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
