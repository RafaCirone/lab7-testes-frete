"""Testes unitários do cupom DESCONTO10 em calcular_frete (roteiro: CT-U06 a CT-U08)."""
import pytest

from frete import calcular_frete


# CT-U06 — REQ-03: DESCONTO10 dá 10% de desconto na taxa de frete
def test_ct_u06_cupom_desconta_10_por_cento_da_taxa():
    assert calcular_frete(100.00, cupom="DESCONTO10") == 13.50


# CT-U07 — REQ-02/REQ-03: com frete grátis o cupom não altera a taxa
def test_ct_u07_cupom_com_frete_gratis_continua_zero():
    assert calcular_frete(250.00, cupom="DESCONTO10") == 0.00


# CT-U08 — REQ-04: cupom desconhecido é rejeitado
def test_ct_u08_cupom_desconhecido_e_rejeitado():
    with pytest.raises(ValueError, match="Cupom inválido"):
        calcular_frete(100.00, cupom="DESCONTO50")
