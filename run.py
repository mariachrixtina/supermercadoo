from flask import Flask
from supermercado.estoque.views import estoque
from supermercado.caixa.views import caixa
from supermercado.pagamento.views import pagamento
from supermercado.ecommerce.views import ecommerce
from supermercado.config import config

app = Flask(__name__)
app.config.from_object(Config)

# Registro das blueprints
app.register_blueprint(estoque, url_prefix='/estoque')
app.register_blueprint(caixa, url_prefix='/caixa')
app.register_blueprint(pagamento, url_prefix='/pagamento')
app.register_blueprint(ecommerce, url_prefix='/ecommerce')

if __name__ == "__main__":
    app.run(debug=True)
