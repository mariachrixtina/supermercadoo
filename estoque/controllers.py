from .models import Produto

# Função para cadastrar produto
def cadastrar_produto(dados_produto):
    try:
        nome = dados_produto['nome']
        preco = float(dados_produto['preco'])
        produto = Produto(nome=nome, preco=preco)
        produto.save()
        return {"mensagem": f"Produto {nome} cadastrado com sucesso!"}
    except Exception as e:
        return {"mensagem": f"Erro ao cadastrar o produto: {str(e)}"}

# Função para listar os produtos
def listar_produtos():
    try:
        produtos = Produto.query.all()
        return [{"nome": produto.nome, "preco": produto.preco} for produto in produtos]
    except Exception as e:
        return {"mensagem": f"Erro ao listar os produtos: {str(e)}"}
