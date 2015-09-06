# Exemplos: Python + BDD
Estes exemplos foram utilizados durante a minha apresentação sobre BDD (Behavior Driven Development) com Python.

## Slides
breve...

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
$ py.test tests/
```
Resultado esperado:
```shell

```
