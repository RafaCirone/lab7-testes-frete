"""Testes funcionais (caixa-preta): o que o cliente paga (roteiro: CT-F01 a CT-F04)."""
import pytest

from frete import calcular_total


# CT-F01 — REQ-01: compra pequena paga frete
def test_ct_f01_compra_pequena_paga_frete():
    carrinho = 80.00
    valor_a_pagar = calcular_total(carrinho)
    assert valor_a_pagar == 95.00


# CT-F02 — REQ-01/REQ-02: um centavo abaixo do limite ainda paga frete
def test_ct_f02_compra_abaixo_do_limite_paga_frete():
    carrinho = 249.99
    valor_a_pagar = calcular_total(carrinho)
    assert valor_a_pagar == pytest.approx(264.99)


# CT-F03 — REQ-02: compra no limite tem frete grátis
def test_ct_f03_compra_no_limite_tem_frete_gratis():
    carrinho = 250.00
    valor_a_pagar = calcular_total(carrinho)
    assert valor_a_pagar == 250.00


# CT-F04 — REQ-01/REQ-02: adicionar um item libera o frete grátis
def test_ct_f04_adicionar_item_libera_frete_gratis():
    carrinho = 180.00
    assert calcular_total(carrinho) == 195.00
    carrinho += 70.00
    assert calcular_total(carrinho) == 250.00
