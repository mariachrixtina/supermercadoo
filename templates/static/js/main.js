// Adiciona produtos ao carrinho
document.querySelectorAll('.adicionar-carrinho').forEach(button => {
    button.addEventListener('click', function() {
        const produtoId = this.getAttribute('data-produto-id');
        
        fetch('/adicionar-carrinho', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ produtoId: produtoId })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
        })
        .catch(error => {
            alert('Erro ao adicionar o produto ao carrinho');
        });
    });
});
