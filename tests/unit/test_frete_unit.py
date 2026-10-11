"""Testes unitários de calcular_frete (roteiro: CT-U01 a CT-U05)."""
from frete import calcular_frete


# CT-U01 — REQ-01: taxa padrão em compra comum
def test_ct_u01_taxa_padrao():
    assert calcular_frete(100.00) == 15.00


# CT-U02 — REQ-01/REQ-02: um centavo abaixo do limite ainda paga frete
def test_ct_u02_um_centavo_abaixo_do_limite():
    assert calcular_frete(249.99) == 15.00


# CT-U03 — REQ-02: exatamente no limite o frete é grátis
def test_ct_u03_frete_gratis_no_limite():
    assert calcular_frete(250.00) == 0.00


# CT-U04 — REQ-02: acima do limite o frete é grátis
def test_ct_u04_frete_gratis_acima_do_limite():
    assert calcular_frete(350.00) == 0.00


# CT-U05 — REQ-02: o limite antigo (R$ 200,00) paga frete
def test_ct_u05_limite_antigo_paga_frete():
    assert calcular_frete(200.00) == 15.00
