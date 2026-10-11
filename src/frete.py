"""Cálculo de frete do checkout — implementa specs/checkout_frete.md."""

FRETE_PADRAO = 15.00  # REQ-01
LIMITE_FRETE_GRATIS = 250.00  # REQ-02


def calcular_frete(subtotal):
    # REQ-02: subtotal maior ou igual ao limite concede frete grátis
    if subtotal >= LIMITE_FRETE_GRATIS:
        return 0.00
    # REQ-01: taxa de frete padrão
    return FRETE_PADRAO


def calcular_total(subtotal):
    # REQ-01: total = subtotal + taxa de frete
    return subtotal + calcular_frete(subtotal)
