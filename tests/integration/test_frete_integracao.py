"""Testes de integração entre calcular_total e calcular_frete (roteiro: CT-I01 a CT-I04)."""
import pytest

import frete
from frete import calcular_frete, calcular_total


# CT-I01 — REQ-01: o total soma a taxa devolvida por calcular_frete
def test_ct_i01_total_soma_taxa_padrao():
    assert calcular_total(100.00) == 115.00


# CT-I02 — REQ-02: total sem taxa quando calcular_frete concede frete grátis
def test_ct_i02_total_sem_taxa_com_frete_gratis():
    assert calcular_total(250.00) == 250.00


# CT-I03 — REQ-01/REQ-02: as duas funções concordam em toda a faixa de valores
@pytest.mark.parametrize("subtotal", [0.00, 100.00, 249.99, 250.00, 1000.00])
def test_ct_i03_total_consistente_com_frete(subtotal):
    assert calcular_total(subtotal) == subtotal + calcular_frete(subtotal)


# CT-I04 — REQ-01: calcular_total realmente consulta calcular_frete
def test_ct_i04_total_consulta_calcular_frete(monkeypatch):
    monkeypatch.setattr(frete, "calcular_frete", lambda *args, **kwargs: 99.00)
    assert calcular_total(10.00) == 109.00
