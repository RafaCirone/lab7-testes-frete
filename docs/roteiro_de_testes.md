# Roteiro de Testes — Sistema de Frete do Checkout

## 1. Objeto de teste

Módulo `src/frete.py`, que implementa `specs/checkout_frete.md`:

- `calcular_frete(subtotal)` — devolve a taxa de frete.
- `calcular_total(subtotal)` — devolve o valor a pagar (subtotal + taxa).

Requisitos cobertos:

- **REQ-01:** o total é o subtotal mais a taxa de frete padrão de R$ 15,00.
- **REQ-02:** subtotal maior ou igual a R$ 250,00 tem frete grátis (taxa R$ 0,00).
- **REQ-03** (exercício 6.5): o cupom `DESCONTO10` dá 10% de desconto sobre a taxa de frete.
- **REQ-04** (exercício 6.5): qualquer outro cupom é rejeitado com o erro "Cupom inválido".

A partir do exercício 6.5 as duas funções aceitam o parâmetro opcional `cupom`.

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

### 4.4 Nova funcionalidade (exercício 6.5) — cupom `DESCONTO10`

| ID | Tipo | Requisito | Objetivo | Entrada / Passos | Resultado esperado | Teste automatizado |
|---|---|---|---|---|---|---|
| CT-U06 | Unitário | REQ-03 | Cupom desconta 10% da taxa | `calcular_frete(100,00, cupom="DESCONTO10")` | taxa = 13,50 | `test_ct_u06_cupom_desconta_10_por_cento_da_taxa` |
| CT-U07 | Unitário | REQ-02, REQ-03 | Cupom com frete grátis não altera a taxa | `calcular_frete(250,00, cupom="DESCONTO10")` | taxa = 0,00 | `test_ct_u07_cupom_com_frete_gratis_continua_zero` |
| CT-U08 | Unitário | REQ-04 | Cupom desconhecido é rejeitado | `calcular_frete(100,00, cupom="DESCONTO50")` | Erro "Cupom inválido" | `test_ct_u08_cupom_desconhecido_e_rejeitado` |
| CT-I05 | Integração | REQ-03 | `calcular_total` repassa o cupom a `calcular_frete` | `calcular_total(100,00, cupom="DESCONTO10")` | 113,50 | `test_ct_i05_total_com_cupom_soma_taxa_com_desconto` |
| CT-I06 | Integração | REQ-04 | A rejeição do cupom chega a quem chamou `calcular_total` | `calcular_total(100,00, cupom="DESCONTO50")` | Erro "Cupom inválido" | `test_ct_i06_total_propaga_rejeicao_de_cupom` |
| CT-F05 | Funcional | REQ-03 | Cliente com cupom paga frete com desconto | Dado um carrinho de R$ 100,00 e o cupom `DESCONTO10`, quando o cliente fecha a compra | Paga R$ 113,50 | `test_ct_f05_cliente_com_cupom_paga_frete_com_desconto` |
| CT-F06 | Funcional | REQ-04 | Cliente com cupom inválido recebe erro | Dado um carrinho de R$ 100,00 e o cupom `PROMO2020`, quando o cliente fecha a compra | Erro "Cupom inválido"; nenhum valor calculado | `test_ct_f06_cliente_com_cupom_invalido_recebe_erro` |
| CT-F07 | Funcional | REQ-01 | Cliente sem cupom continua pagando frete cheio | Dado um carrinho de R$ 100,00 sem cupom, quando o cliente fecha a compra | Paga R$ 115,00 | `test_ct_f07_cliente_sem_cupom_paga_frete_cheio` |

### 4.5 Testes de regressão (exercício 6.5)

| ID | Objetivo | Passos | Resultado esperado |
|---|---|---|---|
| CT-R01 | Garantir que o cupom não afetou frete padrão nem frete grátis | 1. Rodar a suíte completa antes da mudança (linha de base). 2. Implementar a funcionalidade sem editar os arquivos `test_frete_*.py`. 3. Rodar a suíte completa de novo | Os 17 testes dos casos CT-U01 a CT-U05, CT-I01 a CT-I04 e CT-F01 a CT-F04 aprovados nas duas execuções |

## 5. Rastreabilidade

| Requisito | Unitário | Integração | Funcional |
|---|---|---|---|
| REQ-01 | CT-U01, CT-U02 | CT-I01, CT-I03, CT-I04 | CT-F01, CT-F02, CT-F04, CT-F07 |
| REQ-02 | CT-U02, CT-U03, CT-U04, CT-U05, CT-U07 | CT-I02, CT-I03 | CT-F02, CT-F03, CT-F04 |
| REQ-03 | CT-U06, CT-U07 | CT-I05 | CT-F05 |
| REQ-04 | CT-U08 | CT-I06 | CT-F06 |

## 6. Registro de execução

Ambiente: Python 3.13.16, pytest 9.1.1, Linux. Saídas completas em `resultados/`.

| Exercício | Escopo | Casos | Testes executados | Aprovados | Reprovados | Evidência |
|---|---|---|---|---|---|---|
| 6.2 | Unitários | CT-U01 a CT-U05 | 5 | 5 | 0 | `resultados/6.2_testes_unitarios.txt` |
| 6.3 | Integração | CT-I01 a CT-I04 | 8 | 8 | 0 | `resultados/6.3_testes_integracao.txt` |
| 6.4 | Funcionais | CT-F01 a CT-F04 | 4 | 4 | 0 | `resultados/6.4_testes_funcionais.txt` |
| 6.5 | Regressão, linha de base | CT-R01 | 17 | 17 | 0 | `resultados/6.5_testes_regressao.txt` (execução 1) |
| 6.5 | Regressão, após o cupom | CT-R01 e casos da seção 4.4 | 25 | 25 | 0 | `resultados/6.5_testes_regressao.txt` (execução 3) |

O caso CT-I03 roda uma vez para cada um dos cinco subtotais, por isso a integração soma 8 testes para 4 casos.
