# language: pt-br

Funcionalidade: Realizar uma venda
  Sendo um funcionário do caixa
  Posso realizar uma venda
  Para que eu possa faturar e liberar os clientes

  Cenário: Estoque disponível.
    Dado que o estoque da coca-cola é de 50 unidades
    Quando informo uma venda de 40 unidades
    Então a venda é registrada
        E o estoque passa a ser de 10 unidades

  Cenário: Estoque Indisponível.
    Dado que o estoque da coca-cola é de 50 unidades
    Quando informo uma venda de 60 unidades
    Então a venda não é registrada
       E é exibida na tela a mensagem "estoque insuficiente!"
