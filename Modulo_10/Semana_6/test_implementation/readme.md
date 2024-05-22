# Test Implementation Project

testes unitários, testes com mocks e testes BDD (Behavior Driven Development).

Claro, aqui está a versão sem o uso de pessoa verbal:

### Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para implementar a lógica do projeto e os testes.
- **unittest**: Biblioteca padrão do Python para a criação e execução de testes unitários.
- **unittest.mock**: Biblioteca para criar mocks em testes, permitindo simular objetos e seus comportamentos.
- **behave**: Framework para testes BDD (Behavior Driven Development), que permite escrever testes em uma linguagem natural.

### Conceitos Aprendidos

- **Testes Unitários**: Criação e execução de testes que verificam o funcionamento de funções individuais de maneira isolada.
- **Mocks em Testes**: Utilização de mocks para simular comportamentos de objetos e funções, permitindo testar componentes de forma independente.
- **Testes BDD**: Implementação de testes que descrevem o comportamento do sistema em uma linguagem natural, facilitando a compreensão e validação de requisitos de negócio.
- **Configuração de Ambiente Virtual**: Configuração e utilização de um ambiente virtual Python para gerenciar dependências de projetos.

## Configuração do Ambiente


1. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Unix/MacOS
    # source venv/Scripts/activate  # Para Windows
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Executando os Testes

### Testes Unitários



Para executar os testes unitários:
```bash
PYTHONPATH=src python -m unittest test/teste_unitario.py
```

### Testes com Mock



Para executar os testes com mock:
```bash
PYTHONPATH=src python -m unittest test/teste_mock.py
```

### Testes BDD



Para executar os testes BDD:
```bash
PYTHONPATH=src behave test/features
```

## Detalhes dos Testes

### Testes Unitários

Os testes unitários verificam a função de conversão de temperatura em `src/conversao.py`.

#### Exemplos:

1. **Conversão de 0 graus Celsius deve resultar em 32 graus Fahrenheit**:
    ```python
    self.assertEqual(celsius_para_fahrenheit(0), 32)
    ```

2. **Conversão de 100 graus Celsius deve resultar em 212 graus Fahrenheit**:
    ```python
    self.assertEqual(celsius_para_fahrenheit(100), 212)
    ```

![Testes Unitários](utils/Screenshot%202024-05-22%20at%2010.28.43.png)

### Testes com Mock

Os testes com mock simulam a função `obter_temperatura_celsius` para testar a função de conversão sem depender da implementação real.

#### Exemplos:

1. **Simulação de uma função que retorna 0 graus Celsius para verificar a conversão**:
    ```python
    @patch('src.conversao.obter_temperatura_celsius', return_value=0)
    ```

![Testes com Mock](utils/Screenshot%202024-05-22%20at%2010.29.50.png)
### Testes BDD

Os testes BDD verificam o comportamento do sistema utilizando a descrição em linguagem natural definida em `test/features/test_bdd.feature`.

#### Exemplos:

1. **Cenário: Converter 0 graus Celsius para Fahrenheit deve resultar em 32 graus Fahrenheit**:
    ```gherkin
    Given que a temperatura é 0 graus Celsius
    When eu converto para Fahrenheit
    Then o resultado deve ser 32 graus Fahrenheit
    ```

![Testes BDD](utils/Screenshot%202024-05-22%20at%2010.46.26.png)

