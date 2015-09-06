# -*- coding: utf-8 -*-
import pytest
from loja.produto import Produto
from loja.estoque import Estoque
from loja.estoque import EstoqueInsuficienteError
from loja.venda import Venda

class TestEstoque(object):

    def test_estoque_disponivel(self):
        """ Cenário: Estoque disponível.
        Dado que o estoque da coca-cola é de 50 unidades
        Quando informo uma venda de 40 unidades
        Então a venda é registrada
            E o estoque passa a ser de 10 unidades
        """
        # criando o produto
        cocacola = Produto(codigo=13, nome='Coca-cola', preco=5.20)

        # preparando o estoque
        estoque = Estoque()
        estoque.add_produto(produto=cocacola, quantidade=50)

        # preparando a venda
        venda = Venda()
        venda.add_item(produto=cocacola, qtd=40, estoque=estoque)

        # realiza a venda
        venda.realizar()

        # asserções do teste
        assert venda.foi_registrada() == True
        assert estoque.quantos(produto_codigo=13) == 10

    def test_estoque_indisponivel(self):
        """ Cenário: Estoque Indisponível.
        Dado que o estoque da coca-cola é de 50 unidades
        Quando informo uma venda de 60 unidades
        Então a venda não é registrada
             E é exibida na tela a mensagem "estoque insuficiente!"
        """
        # criando o produto
        cocacola = Produto(codigo=13, nome='Coca-cola', preco=5.20)

        # preparando o estoque
        estoque = Estoque()
        estoque.add_produto(produto=cocacola, quantidade=50)

        # preparando a venda
        venda = Venda()
        venda.add_item(produto=cocacola, qtd=60, estoque=estoque)

        # realiza a venda
        with pytest.raises(EstoqueInsuficienteError) as exception:
            venda.realizar()

        # asserções do teste
        assert venda.foi_registrada() == False
        assert "estoque insuficiente!" == str(exception.value)

    @pytest.mark.xfail(raises=EstoqueInsuficienteError)
    def test_estoque_disponivel_venda_limitada_30(self):
        """ Cenário: Estoque disponível, venda limitada a 30.
        Dado que o estoque da coca-cola é de 50 unidades
            E a venda máxima por cliente é limitada a 30 unidades
        Quando informo uma venda de 20 unidades
        Então a venda é registrada
            E o estoque passa a ser de 30 unidades
        """
        # criando o produto
        cocacola = Produto(codigo=13, nome='Coca-cola', preco=5.20)

        # preparando o estoque
        estoque = Estoque()
        estoque.add_produto(produto=cocacola, quantidade=50)

        # preparando a venda
        venda = Venda(lim_cliente=30)
        venda.add_item(produto=cocacola, qtd=20, estoque=estoque)

        # realiza a venda
        venda.realizar()

        assert venda.foi_registrada() == True
        assert estoque.quantos(produto_codigo=13) == 30
