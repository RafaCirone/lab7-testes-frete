# Lab 6 — Testes e Qualidade de Software (sistema de frete)

Exercícios 6.1 a 6.5 aplicados ao sistema de cálculo de frete do checkout
(código de origem: repositório `lab6-sdd-frete`).

| Exercício | Entregável | Onde está |
|---|---|---|
| 6.1 Roteiro de Testes | Roteiro com casos de teste | `docs/roteiro_de_testes.md` |
| 6.2 Teste Unitário | Testes e resultados | `tests/unit/`, `resultados/6.2_testes_unitarios.txt` |
| 6.3 Teste de Integração | Testes e resultados | `tests/integration/`, `resultados/6.3_testes_integracao.txt` |
| 6.4 Teste Funcional | Testes e resultados | `tests/functional/`, `resultados/6.4_testes_funcionais.txt` |
| 6.5 Testes de Regressão | Código alterado e resultados | `src/frete.py`, `resultados/6.5_testes_regressao.txt` |

## Como rodar

```
pip install pytest
pytest -v                    # suíte completa
pytest -v tests/unit         # só unitários
pytest -v tests/integration  # só integração
pytest -v tests/functional   # só funcionais
```

## Exercício 6.5 — nova funcionalidade

O enunciado pede "investimento em poupança" para o sistema bancário. Como este
laboratório foi feito sobre o sistema de frete, a funcionalidade nova escolhida foi o
cupom `DESCONTO10` (10% de desconto sobre a taxa de frete), especificada como
REQ-03 e REQ-04 em `specs/checkout_frete.md` antes de qualquer código.

Os 17 testes dos exercícios 6.2 a 6.4 serviram de suíte de regressão: rodaram antes
e depois da mudança, sem edição, e passaram nas duas vezes.

## Ambiente dos resultados registrados

Python 3.13.16, pytest 9.1.1, Linux.
