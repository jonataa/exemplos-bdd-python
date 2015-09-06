class VendaItem(object):

    def __init__(self, produto, qtd, estoque):
        self.produto = produto
        self.qtd = qtd
        self.estoque = estoque

class Venda(object):

    items = []

    def __init__(self, lim_cliente=30, lim_compra_cartao=20.00):
        self.lim_cliente = lim_cliente
        self.lim_compra_cartao = lim_compra_cartao
        self.registrada = False

    def add_item(self, produto, qtd, estoque):
        self.items.append(VendaItem(produto, qtd, estoque))

    def foi_registrada(self):
        return self.registrada

    def realizar(self):
        for item in self.items:
            item.estoque.retirar(item.produto, item.qtd)
        self.registrada = True

    def calcular_total(self):        
        return sum(item.produto.preco for item in self.items)
