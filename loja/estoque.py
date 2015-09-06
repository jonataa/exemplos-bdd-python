class EstoqueInsuficienteError(Exception):

    def __init__(self, value='estoque insuficiente!'):
        self.value = value

    def __str__(self):
        return self.value

class EstoqueItem(object):

    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

class Estoque(object):

    estoque = {}

    def add_produto(self, produto, quantidade):
        self.estoque[produto.codigo] = EstoqueItem(produto, quantidade)

    def retirar(self, produto, qtd):
        if self.quantos(produto.codigo) < qtd:
            raise EstoqueInsuficienteError()
        self.estoque[produto.codigo].qtd -= qtd

    def quantos(self, produto_codigo):
        return self.estoque[produto_codigo].qtd
