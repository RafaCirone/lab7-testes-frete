"""Testes funcionais do cupom na visão do cliente (roteiro: CT-F05 a CT-F07)."""
import pytest

from frete import calcular_total


# CT-F05 — REQ-03: cliente com cupom paga frete com desconto
def test_ct_f05_cliente_com_cupom_paga_frete_com_desconto():
    carrinho = 100.00
    valor_a_pagar = calcular_total(carrinho, cupom="DESCONTO10")
    assert valor_a_pagar == 113.50


# CT-F06 — REQ-04: cliente com cupom inválido recebe o erro e nada é calculado
def test_ct_f06_cliente_com_cupom_invalido_recebe_erro():
    carrinho = 100.00
    with pytest.raises(ValueError, match="Cupom inválido"):
        calcular_total(carrinho, cupom="PROMO2020")


# CT-F07 — REQ-01: cliente sem cupom continua pagando o frete cheio
def test_ct_f07_cliente_sem_cupom_paga_frete_cheio():
    carrinho = 100.00
    assert calcular_total(carrinho) == 115.00
