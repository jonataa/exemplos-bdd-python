# -*- coding: utf-8 -*-

class Pagamento(object):
    CARTAO_CREDITO = 'cartão de crédito'
    CARTAO_DEBITO = 'cartão de débito'
    DINHEIRO = 'dinheiro'
    MSG_MINIMO_CARTAO = 'Para valores inferiores a 20 reais somente dinheiro.'

    def __init__(self, total, meio_pagamento=None):
        self.meio_pagamento = self.DINHEIRO if meio_pagamento is None else meio_pagamento
        self.check(total)

    def check(self, total):
        if self.meio_pagamento in [self.CARTAO_CREDITO, self.CARTAO_DEBITO]:
            if total <= 20:
                raise MeioPagamentoInvalidoError(self.MSG_MINIMO_CARTAO)

class MeioPagamentoInvalidoError(Exception):

    prefixo = "Meio de pagamento inválido! %s"

    def __init__(self, motivo):
        self.value = self.prefixo % motivo

    def __str__(self):
        return self.value
