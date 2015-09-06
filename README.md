# Exemplos: Python + BDD
Estes exemplos foram utilizados durante a minha apresentação sobre BDD (Behavior Driven Development) com Python.

## Slides
breve...

## Pré-Requisitos
* [Instalando o Lettuce](http://lettuce.it/intro/install.html)
* [Instalando o pytest](http://pytest.org/latest/getting-started.html)

Para instalar todas as dependências via ```pip```, apenas execute:

```shell
$ pip install -r requirements.txt
```

## Introdução ao pytest
breve...

## Cenários

Cenário: Estoque disponível.  
**Dado que** o estoque da coca-cola é de 50 unidades  
**Quando** informo uma venda de 40 unidades  
**Então** a venda é registrada  
  **E** o estoque passa a ser de 10 unidades

Cenário: Estoque Indisponível.  
**Dado que** o estoque da coca-cola é de 50 unidades  
**Quando** informo uma venda de 60 unidades  
**Então** a venda não é registrada  
  **E** é exibida na tela a mensagem "estoque
insuficiente!"  

Cenário: Estoque disponível, venda limitada a 30.  
**Dado que** o estoque da coca-cola é de 50 unidades  
  **E** a venda máxima por cliente é limitada a 30 unidades  
**Quando** informo uma venda de 20 unidades   
**Então** a venda é registrada  
  **E** o estoque passa a ser de 30 unidades  

Cenário: Venda com cartão indisponível para valores abaixo de 20,00.  
**Dado que** o valor da venda é de 10,00  
  **E** o valor mínimo de vendas para cartão é de 20,00  
**Quando** informo que o meio de pagamento é cartão de crédito  
  **OU** informo que o meio de pagamento é cartão de débito  
**Então** a venda não é registrada  
  **E** é exibida na tela a mensagem "Meio de pagamento inválido! Para valores
inferiores a 20 reais somente dinheiro.  

## Executando os testes unitários
Uma vez que esteja com o ```pytest``` instalado, apenas digite:
```shell
$ py.test tests/units/test_estoque.py

============================= test session starts ==============================
platform darwin -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
rootdir: /Users/jweber/dev/projects/exemplos-bdd-uefs/tests, inifile:
collected 3 items

tests/test_estoque.py ..x

===================== 2 passed, 1 xfailed in 0.02 seconds ======================
```
```shell
$ py.test tests/units/test_venda.py

============================= test session starts ==============================
platform darwin -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
rootdir: /Users/jweber/dev/projects/exemplos-bdd-uefs/tests, inifile:
collected 1 items

tests/test_venda.py .

=========================== 1 passed in 0.01 seconds ===========================
```
