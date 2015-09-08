class EstoqueInsuficienteError(Exception):

    def __init__(self, value='estoque insuficiente!'):
        self.value = value

    def __str__(self):
        return self.value

class EstoqueItem(object):

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def quantos(self):
        return self.quantidade

class Estoque(object):

    itens = {}

    def add_produto(self, produto, quantidade):
        self.itens[produto.codigo] = EstoqueItem(produto, quantidade)

    def retirar(self, produto, quantidade):
        item = self[produto.codigo]
        if quantidade > item.quantos():
            raise EstoqueInsuficienteError()
        item.quantidade -= quantidade

    def quantos(self, produto_codigo):
        return self[produto_codigo].quantos()

    def __getitem__(self, key):
        return self.itens[key]
