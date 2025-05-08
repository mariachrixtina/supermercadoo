from flask import render_template

# Rota para exibir a página de métodos de pagamento
@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')
