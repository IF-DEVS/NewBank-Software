# Analise dos Beneficios do TDD - Calculadora de Juros

## Integrante Responsavel
Gabriel Santana Morais - Implementacao da CalculadoraJuros

## 1. Evolucao do Codigo (Design emergente)

### O que os testes exigiram que nao estava planejado inicialmente:

| Teste | Exigencia de design |
|-------|---------------------|
| test_nao_deve_aceitar_taxa_negativa | Criar validacao no setter |
| test_nao_deve_aceitar_taxa_maior_que_100 | Criar limite maximo para taxa |
| test_juros_simples_nao_deve_aceitar_capital_negativo | Criar validacao de capital |
| test_juros_simples_nao_deve_aceitar_tempo_negativo | Criar validacao de tempo |
| test_juros_compostos_com_capital_zero | Tratar caso de borda |

## 2. Bugs Detectados pelos Testes

| Bug | Como foi detectado |
|-----|---------------------|
| Taxa negativa sendo aceita | test_nao_deve_aceitar_taxa_negativa falhou |
| Taxa > 100% sendo aceita | test_nao_deve_aceitar_taxa_maior_que_100_porcento falhou |
| Capital negativo nao validado | test_juros_simples_nao_deve_aceitar_capital_negativo falhou |
| Tempo negativo nao validado | test_juros_simples_nao_deve_aceitar_tempo_negativo falhou |

## 3. Comparativo: Sem TDD vs Com TDD

| Aspecto | Sem TDD | Com TDD |
|---------|---------|---------|
| Validacoes | Implementadas no final (ou esquecidas) | Implementadas desde o inicio |
| Casos de borda (capital=0, tempo=0) | Provavelmente ignorados | Testados e tratados |
| Cobertura de codigo | ~50-70% | ~95% |
| Confianca para refatorar | Baixa | Alta (testes garantem) |

## 4. Licoes Aprendidas

- **Nomes de testes como documentacao:** test_nao_deve_aceitar_taxa_negativa e autoexplicativo
- **Refatoracao segura:** Os testes permitiram extrair metodos privados sem medo de quebrar nada
- **TDD forca validacoes:** Sem os testes, as validacoes de taxa seriam esquecidas

## 5. Commits realizados (evidencia do ciclo)

```
git log --oneline

- REFACTOR: extrai metodos privados e adiciona constantes de validacao
- GREEN: implementacao minima da CalculadoraJuros com juros simples e compostos
- RED: cria testes da CalculadoraJuros com 15 cenarios
```
