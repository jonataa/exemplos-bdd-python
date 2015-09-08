# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import world
from loja.produto import Produto
from loja.estoque import Estoque
from loja.estoque import EstoqueInsuficienteError
from loja.venda import Venda

@step(u'Dado que o estoque da coca-cola é de 50 unidades')
def dado_que_o_estoque_da_coca_cola_e_de_50_unidades(step):
    world.cocacola = Produto(codigo=13, nome='Coca-cola', preco=5.20)
    world.estoque = Estoque()
    world.estoque.add_produto(produto=world.cocacola, quantidade=50)

@step(u'Quando informo uma venda de 40 unidades')
def quando_informo_uma_venda_de_40_unidades(step):
    world.venda = Venda()
    world.venda.add_item(produto=world.cocacola, qtd=40, estoque=world.estoque)
    world.venda.realizar()

@step(u'Então a venda é registrada')
def entao_a_venda_e_registrada(step):
    assert world.venda.foi_registrada() is True

@step(u'E o estoque passa a ser de 10 unidades')
def e_o_estoque_passa_a_ser_de_10_unidades(step):
    codigo_produto = world.cocacola.codigo
    assert world.estoque.quantos(codigo_produto) == 10

@step(u'Quando informo uma venda de 60 unidades')
def quando_informo_uma_venda_de_60_unidades(step):
    world.venda = Venda()
    world.venda.add_item(produto=world.cocacola, qtd=60, estoque=world.estoque)
    try:
        world.venda.realizar()
    except EstoqueInsuficienteError as e:
        world.mensagem = e.value

@step(u'Então a venda não é registrada')
def entao_a_venda_nao_e_registrada(step):
    assert world.venda.foi_registrada() is False

@step(u'E é exibida na tela a mensagem "([^"]*)"')
def e_e_exibida_na_tela_a_mensagem_group1(step, expected):
    assert world.mensagem == expected
