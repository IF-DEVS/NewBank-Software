# Etapa 4 — Análise dos Benefícios do TDD

## NewBank · Disciplina: Teste de Software

---

## 1. Evolução do Código: Como o Design Emergiu dos Testes

O desenvolvimento orientado por testes forçou decisões de design que, em uma abordagem tradicional, provavelmente só apareceriam após refatorações tardias.

### ContaBancaria
O primeiro teste — criar uma conta com saldo inicial — já definiu a assinatura do construtor (`saldo_inicial`, `numero_conta`). O teste de depósito com valor negativo exigiu que a validação existisse *antes mesmo de o método estar completo*, o que naturalmente levou à separação entre a regra de negócio (valor positivo) e a operação em si. A exceção customizada `SaldoInsuficienteException` surgiu do teste de saque com saldo insuficiente: percebemos que um `ValueError` genérico não comunicaria bem o problema ao chamador.

### Transferencia
Os testes de validação (mesma conta, valor negativo, saldo insuficiente) guiaram a separação em dois métodos privados: `_validar_contas()` e `_validar_valor()`. Sem o TDD, seria tentador colocar tudo no `executar()`. Os testes tornaram a separação de responsabilidades uma consequência natural.

### Extrato + Transacao
A classe `Transacao` surgiu indiretamente dos testes de `Extrato`. Ao escrever o teste `test_adicionar_transacao_registra_uma_transacao`, ficou claro que o extrato não deveria receber valores brutos, mas sim objetos estruturados. Isso levou à criação da classe `Transacao` e do enum `CategoriaTransacao`, tornando o modelo mais rico e seguro.

### CalculadoraJuros
A separação entre métodos públicos (`calcular_juros_simples`, `calcular_juros_compostos`) e privados (`_calcular_juros_simples`, `_calcular_juros_compostos`) emergiu porque os testes de validação de entrada precisavam ser testados isoladamente das operações matemáticas. O design resultante ficou mais limpo do que seria em uma implementação livre.

---

## 2. Bugs Encontrados pelos Testes Antes da Integração

| # | Classe | Bug identificado | Como o teste revelou |
|---|--------|-----------------|----------------------|
| 1 | `CalculadoraJuros` | `__init__` escrito como `_init_` (um underscore) | Ao instanciar `CalculadoraJuros(taxa=0.10)` no `setup_method`, a taxa nunca era atribuída — `get_taxa()` lançava `AttributeError` |
| 2 | `ContaBancaria` | Ausência de validação para depósito de valor zero | O teste `test_depositar_zero_deve_lancar_excecao` falhou (Red) até a condição `valor <= 0` ser implementada corretamente |
| 3 | `Extrato` | Valor `None` passava pela checagem `isinstance` | `isinstance(None, (int, float))` retorna `False`, mas o erro lançado deveria ser `ValueError`; o teste `test_adicionar_transacao_com_valor_none` confirmou o comportamento correto |
| 4 | `Transferencia` | Ausência de validação para valor zero | Coberto indiretamente pelo teste de valor negativo; a condição `<= 0` previne ambos |

---

## 3. Comparativo: Sem TDD vs. Com TDD

| Aspecto | Sem TDD | Com TDD |
|---------|---------|---------|
| **Quando os bugs aparecem** | Na integração ou em produção | No ciclo Red, antes do código existir |
| **Cobertura de testes** | Depende da disciplina do time; tende a ser baixa | Alta por construção — cada funcionalidade nasce com teste |
| **Design das classes** | Tende a acumular responsabilidades; refatorações custosas | Interfaces enxutas emergem naturalmente dos testes |
| **Confiança para refatorar** | Baixa — risco de quebrar comportamento existente | Alta — a suite de testes funciona como rede de segurança |
| **Documentação** | Separada do código, frequentemente desatualizada | Os testes *são* a documentação viva do comportamento esperado |
| **Custo de mudança** | Cresce com o tempo | Relativamente estável — testes apontam o impacto de mudanças |

### Exemplo concreto
Sem TDD, a classe `CalculadoraJuros` provavelmente seria escrita de uma vez, com o bug do `_init_` passando despercebido até o primeiro teste manual. Com TDD, o `setup_method` dos testes quebrou imediatamente (Red), apontando o erro antes de qualquer integração.

---

## 4. Lições Aprendidas pelo Grupo

**Escrever o teste primeiro é desconfortável no começo, mas compensa.** A resistência inicial de "escrever um teste para algo que ainda não existe" diminuiu conforme percebemos que o teste funciona como uma especificação executável — ele força a pensar na interface antes da implementação.

**Nomes de testes são documentação.** O padrão `test_deve_[acao]_quando_[condicao]` eliminou ambiguidades. Quando um teste falha, o nome já descreve o que está errado sem precisar ler o código.

**Commits pequenos tornam o histórico legível.** Fazer commit a cada ciclo Red → Green → Refactor criou um histórico que conta a história do desenvolvimento. É possível ver exatamente em que ponto cada regra de negócio foi adicionada.

**TDD não substitui code review — os dois se complementam.** Encontramos casos em que o teste passava mas o código estava mais complexo do que precisava. A fase de Refactor, combinada com revisão entre os integrantes, foi essencial para manter a qualidade.

**Exceções customizadas valem o esforço.** `SaldoInsuficienteException` deixou os testes mais expressivos e o código de integração mais fácil de tratar do que um `ValueError` genérico faria.
