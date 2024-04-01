## Criando e executando testes para código gerenciado

### Introdução:

  - Este relatório documenta o processo de criação e execução de testes de unidade para código C# gerenciado, utilizando a estrutura de teste de unidade da Microsoft (MSTest) e o Gerenciador de Testes.
  -  O objetivo é garantir que o código funcione conforme o esperado e detectar erros com mais facilidade.

### Tecnologias envolvidas
 - IDE (Integrated Development Environment) utilizada para desenvolvimento de software.
 - Linguagem de programação utilizada para o código gerenciado.
 - Estrutura de teste de unidade da Microsoft para código gerenciado.
 - Ferramenta do Visual Studio para executar e gerenciar testes de unidade.

#### Passos realizados:

### 1. Criação do projeto para teste:

 - Criado um projeto de aplicativo de console C# chamado "Bank".

 - Implementada a classe BankAccount com métodos para gerenciar o saldo da conta, incluindo Debit (débito) e Credit (crédito).

 - Corrigido um erro no método Debit que adicionava o valor do débito ao saldo em vez de subtraí-lo.

### 2. Criação do projeto de teste de unidade:

 - Criado um projeto de teste de unidade MSTest chamado "BankTests".
Adicionada uma referência ao projeto "Bank" para que os testes pudessem acessar a classe BankAccount.

### 3. Criação da classe de teste:

 - Criada a classe BankAccountTests com o atributo [TestClass] para indicar que se trata de uma classe de teste de unidade.
 - Adicionada a instrução using BankAccountNS; para evitar a necessidade de usar nomes de classes totalmente qualificados.

### 4 Criação dos métodos de teste
 - Implementados vários métodos de teste com o atributo [TestMethod] para verificar diferentes comportamentos da classe BankAccount:

 - Debit_WithValidAmount_UpdatesBalance: verifica se o método Debit atualiza o saldo corretamente quando um valor válido é debitado.

 - Debit_WhenAmountIsLessThanZero_ShouldThrowArgumentOutOfRange: verifica se o método Debit lança uma exceção ArgumentOutOfRangeException quando o valor do débito é menor que zero.

 - Debit_WhenAmountIsMoreThanBalance_ShouldThrowArgumentOutOfRange: verifica se o método Debit lança uma exceção ArgumentOutOfRangeException quando o valor do débito é maior que o saldo da conta.

 - Credit_WithValidAmount_UpdatesBalance: verifica se o método Credit adiciona um valor válido ao saldo da conta corretamente.

 - Credit_WhenAmountIsLessThanZero_ShouldThrowArgumentOutOfRange: verifica se o método Credit lança uma exceção ArgumentOutOfRangeException quando o valor do crédito é menor que zero.


### 5  Execução dos testes:
 - Utilizado o comando dotnet test para executar os testes de unidade no projeto "BankTests".

 - Analisados os resultados dos testes e corrigidos erros no código da classe BankAccount conforme necessário.

### Conceitos aprendidos:

 - testes de software que verificam o comportamento de unidades individuais de código (métodos, classes, etc.).

 - conjunto de ferramentas e bibliotecas que facilitam a criação e execução de testes de unidade.

 - padrão de organização de testes de unidade em três etapas: Arrange (preparar), Act (agir) e Assert (afirmar).
 
 - declarações que verificam se o resultado de um teste corresponde ao esperado.

### Conclusão
A implementação de testes de unidade para a classe BankAccount ajudou a garantir que o código funcione conforme o esperado e a detectar erros. O uso de testes de unidade é uma prática importante para o desenvolvimento de software de alta qualidade.

