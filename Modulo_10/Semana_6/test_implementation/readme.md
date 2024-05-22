# Test Implementation Project

testes unitários, testes com mocks e testes BDD (Behavior Driven Development).


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

![Testes Unitários](utils/Screenshot_2024-05-22_at_10.28.43.png)

### Testes com Mock

Os testes com mock simulam a função `obter_temperatura_celsius` para testar a função de conversão sem depender da implementação real.

#### Exemplos:

1. **Simulação de uma função que retorna 0 graus Celsius para verificar a conversão**:
    ```python
    @patch('src.conversao.obter_temperatura_celsius', return_value=0)
    ```

![Testes com Mock](path/to/utils/Screenshot_2024-05-22_at_10.29.50.png)

### Testes BDD

Os testes BDD verificam o comportamento do sistema utilizando a descrição em linguagem natural definida em `test/features/test_bdd.feature`.

#### Exemplos:

1. **Cenário: Converter 0 graus Celsius para Fahrenheit deve resultar em 32 graus Fahrenheit**:
    ```gherkin
    Given que a temperatura é 0 graus Celsius
    When eu converto para Fahrenheit
    Then o resultado deve ser 32 graus Fahrenheit
    ```

![Testes BDD](utils/Screenshot_2024-05-22_at_10.46.26.png)

