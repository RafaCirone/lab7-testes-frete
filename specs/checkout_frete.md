# Especificação: Checkout — Cálculo de Frete

Fonte única da verdade (SSOT) para o cálculo de frete no checkout. Notação EARS.

## Requisitos

**REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.

**REQ-02 (IF/THEN):** IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

**REQ-03 (Event-Driven):** WHEN o cliente informar o cupom `DESCONTO10`, THE SYSTEM SHALL aplicar 10% de desconto sobre a taxa de frete.

**REQ-04 (IF/THEN):** IF o cupom informado não for `DESCONTO10`, THEN THE SYSTEM SHALL rejeitar a operação com o erro "Cupom inválido".
