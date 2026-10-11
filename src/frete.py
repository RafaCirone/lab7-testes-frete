"""Cálculo de frete do checkout — implementa specs/checkout_frete.md."""

FRETE_PADRAO = 15.00  # REQ-01
LIMITE_FRETE_GRATIS = 250.00  # REQ-02
CUPOM_DESCONTO10 = "DESCONTO10"  # REQ-03
DESCONTO_CUPOM = 0.10  # REQ-03


def calcular_frete(subtotal, cupom=None):
    # REQ-04: cupom diferente de DESCONTO10 é rejeitado
    if cupom is not None and cupom != CUPOM_DESCONTO10:
        raise ValueError("Cupom inválido")
    # REQ-02: subtotal maior ou igual ao limite concede frete grátis
    if subtotal >= LIMITE_FRETE_GRATIS:
        return 0.00
    # REQ-03: DESCONTO10 dá 10% de desconto sobre a taxa de frete
    if cupom == CUPOM_DESCONTO10:
        return round(FRETE_PADRAO * (1 - DESCONTO_CUPOM), 2)
    # REQ-01: taxa de frete padrão
    return FRETE_PADRAO


def calcular_total(subtotal, cupom=None):
    # REQ-01: total = subtotal + taxa de frete
    return subtotal + calcular_frete(subtotal, cupom)
