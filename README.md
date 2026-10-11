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
