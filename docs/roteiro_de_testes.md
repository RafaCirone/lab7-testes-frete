# Roteiro de Testes — Sistema de Frete do Checkout

## 1. Objeto de teste

Módulo `src/frete.py`, que implementa `specs/checkout_frete.md`:

- `calcular_frete(subtotal)` — devolve a taxa de frete.
- `calcular_total(subtotal)` — devolve o valor a pagar (subtotal + taxa).

Requisitos cobertos:

- **REQ-01:** o total é o subtotal mais a taxa de frete padrão de R$ 15,00.
- **REQ-02:** subtotal maior ou igual a R$ 250,00 tem frete grátis (taxa R$ 0,00).

## 2. Tipos de teste

| Tipo | O que verifica neste sistema | Pasta |
|---|---|---|
| Unitário | `calcular_frete` isolada, uma regra por caso | `tests/unit/` |
| Integração | `calcular_total` trabalhando junto com `calcular_frete` | `tests/integration/` |
| Funcional | O comportamento visto pelo cliente (caixa-preta): carrinho entra, valor a pagar sai | `tests/functional/` |

## 3. Ambiente e execução

- Python 3 e pytest; sem outras dependências.
- Pré-condição geral: repositório clonado e `pytest` instalado.
- Comando: `pytest -v` (ou por pasta, ver `README.md`).
- Critério de aprovação: 100% dos casos com resultado obtido igual ao esperado.

## 4. Casos de teste

### 4.1 Testes unitários — `calcular_frete`

| ID | Requisito | Objetivo | Entrada | Resultado esperado | Teste automatizado |
|---|---|---|---|---|---|
| CT-U01 | REQ-01 | Cobrar a taxa padrão em compra comum | subtotal = 100,00 | taxa = 15,00 | `test_ct_u01_taxa_padrao` |
| CT-U02 | REQ-01, REQ-02 | Valor limite: um centavo abaixo do frete grátis | subtotal = 249,99 | taxa = 15,00 | `test_ct_u02_um_centavo_abaixo_do_limite` |
| CT-U03 | REQ-02 | Valor limite: exatamente no limite | subtotal = 250,00 | taxa = 0,00 | `test_ct_u03_frete_gratis_no_limite` |
| CT-U04 | REQ-02 | Frete grátis acima do limite | subtotal = 350,00 | taxa = 0,00 | `test_ct_u04_frete_gratis_acima_do_limite` |
| CT-U05 | REQ-02 | Limite antigo (R$ 200,00) não dá mais frete grátis | subtotal = 200,00 | taxa = 15,00 | `test_ct_u05_limite_antigo_paga_frete` |

### 4.2 Testes de integração — `calcular_total` com `calcular_frete`

| ID | Requisito | Objetivo | Entrada / Passos | Resultado esperado | Teste automatizado |
|---|---|---|---|---|---|
| CT-I01 | REQ-01 | Total soma a taxa devolvida por `calcular_frete` | `calcular_total(100,00)` | 115,00 | `test_ct_i01_total_soma_taxa_padrao` |
| CT-I02 | REQ-02 | Total sem taxa quando `calcular_frete` concede frete grátis | `calcular_total(250,00)` | 250,00 | `test_ct_i02_total_sem_taxa_com_frete_gratis` |
| CT-I03 | REQ-01, REQ-02 | As duas funções concordam em toda a faixa de valores | Para 0,00; 100,00; 249,99; 250,00; 1000,00: comparar `calcular_total(s)` com `s + calcular_frete(s)` | Iguais em todos os valores | `test_ct_i03_total_consistente_com_frete` |
| CT-I04 | REQ-01 | `calcular_total` realmente consulta `calcular_frete` | 1. Substituir `calcular_frete` por um dublê que devolve 99,00. 2. Chamar `calcular_total(10,00)` | 109,00 | `test_ct_i04_total_consulta_calcular_frete` |

### 4.3 Testes funcionais — visão do cliente

| ID | Requisito | Cenário | Passos | Resultado esperado | Teste automatizado |
|---|---|---|---|---|---|
| CT-F01 | REQ-01 | Compra pequena paga frete | Dado um carrinho de R$ 80,00, quando o cliente fecha a compra | Paga R$ 95,00 | `test_ct_f01_compra_pequena_paga_frete` |
| CT-F02 | REQ-01, REQ-02 | Compra um centavo abaixo do limite | Dado um carrinho de R$ 249,99, quando o cliente fecha a compra | Paga R$ 264,99 | `test_ct_f02_compra_abaixo_do_limite_paga_frete` |
| CT-F03 | REQ-02 | Compra no limite ganha frete grátis | Dado um carrinho de R$ 250,00, quando o cliente fecha a compra | Paga R$ 250,00 | `test_ct_f03_compra_no_limite_tem_frete_gratis` |
| CT-F04 | REQ-01, REQ-02 | Cliente adiciona item para ganhar frete grátis | 1. Carrinho de R$ 180,00: consultar o valor a pagar. 2. Adicionar item de R$ 70,00 (carrinho R$ 250,00): consultar de novo | 1. R$ 195,00. 2. R$ 250,00 | `test_ct_f04_adicionar_item_libera_frete_gratis` |

## 5. Rastreabilidade

| Requisito | Unitário | Integração | Funcional |
|---|---|---|---|
| REQ-01 | CT-U01, CT-U02 | CT-I01, CT-I03, CT-I04 | CT-F01, CT-F02, CT-F04 |
| REQ-02 | CT-U02, CT-U03, CT-U04, CT-U05 | CT-I02, CT-I03 | CT-F02, CT-F03, CT-F04 |
