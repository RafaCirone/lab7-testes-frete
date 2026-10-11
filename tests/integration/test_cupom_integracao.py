"""Testes de integração do cupom entre calcular_total e calcular_frete (roteiro: CT-I05 e CT-I06)."""
import pytest

from frete import calcular_total


# CT-I05 — REQ-03: calcular_total repassa o cupom e soma a taxa com desconto
def test_ct_i05_total_com_cupom_soma_taxa_com_desconto():
    assert calcular_total(100.00, cupom="DESCONTO10") == 113.50


# CT-I06 — REQ-04: a rejeição do cupom em calcular_frete chega a quem chamou calcular_total
def test_ct_i06_total_propaga_rejeicao_de_cupom():
    with pytest.raises(ValueError, match="Cupom inválido"):
        calcular_total(100.00, cupom="DESCONTO50")
