# -*- coding: utf-8 -*-
import pytest
from loja.produto import Produto
from loja.estoque import Estoque
from loja.venda import Venda
from loja.pagamento import Pagamento
from loja.pagamento import MeioPagamentoInvalidoError

class TestVenda(object):

    def test_venda_cartao_indisp_valor_abaixo_vinte(self):
        """ Cenário: Venda com cartão indisponível para valores
        abaixo de 20,00.
        Dado que o valor da venda é de 10,00
             E o valor mínimo de vendas para cartão é de 20,00
        Quando informo que o meio de pagamento é cartão de crédito
             OU informo que o meio de pagamento é cartão de débito
        Então a venda não é registrada
             E é exibida na tela a mensagem "Meio de pagamento
             inválido! Para valores inferiores a 20 reais somente dinheiro."
        """
        # criando o produto
        cocacola = Produto(codigo=13, nome='Coca-cola', preco=5.00)
        fanta = Produto(codigo=14, nome='Fanta', preco=5.00)

        # preparando o estoque
        estoque = Estoque()
        estoque.add_produto(produto=cocacola, quantidade=50)
        estoque.add_produto(produto=fanta, quantidade=40)

        # preparando a venda
        venda = Venda(lim_compra_cartao=20.00)
        venda.add_item(produto=cocacola, qtd=1, estoque=estoque)
        venda.add_item(produto=fanta, qtd=1, estoque=estoque)

        # meio de pagamento
        with pytest.raises(MeioPagamentoInvalidoError) as expt_credito:
            Pagamento(venda.calcular_total(), Pagamento.CARTAO_CREDITO)

        with pytest.raises(MeioPagamentoInvalidoError) as expt_debito:
            Pagamento(venda.calcular_total(), Pagamento.CARTAO_DEBITO)
                    
        msg_esperada = 'Meio de pagamento inválido! Para valores inferiores a 20 reais somente dinheiro.'

        # asserções do teste
        assert venda.foi_registrada() is False
        assert venda.calcular_total() == 10
        assert msg_esperada in (str(expt_credito.value) and str(expt_debito.value))
