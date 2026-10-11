# Especificação: Checkout — Cálculo de Frete

Fonte única da verdade (SSOT) para o cálculo de frete no checkout. Notação EARS.

## Requisitos

**REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.

**REQ-02 (IF/THEN):** IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
