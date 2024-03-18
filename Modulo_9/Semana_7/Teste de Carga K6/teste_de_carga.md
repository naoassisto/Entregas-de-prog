# K6


### Notas para a atividade:
 - Ja Implementei diretamente no projeto, logo o relatorio esta extenso pois ele testa todos os endpoints do nosso projeto. 

## Instalação e Uso

### Passo a Passo
1. Instalar o k6:

`npm install -g k6`

2. Criar um novo projeto k6:

`k6 new load_test`

3. Uso:

**Imports**
```javascript
import http from 'k6/http';
import { sleep, group } from 'k6';
```
**Definição de carga**

```javascript
export const options = {
    vus: 10, // 10 virtual users
    duration: '5m', // Test duration of 5 minutes
};
```
**Def Teste de Carga**
```javascript
export default function () {
    group('Load Test', () => {
        http.get('http://localhost:3000');
    });

    sleep(1); // Add a small delay between requests
}
```

JavaScript
4. Executar o teste de carga:

``k6 run load_test.js``


5. Gerar um relatório:

k6 report > ``load_test_report.html``

## Tecnologia e Conceitos Aprendidos
**k6:** é uma ferramenta de teste de carga e estresse de código aberto que permite simular cargas de usuários em um sistema para avaliar seu desempenho. O k6 usa JavaScript como linguagem de script, o que o torna fácil de aprender e usar.

**Teste de Carga:** mede o desempenho de um sistema sob uma carga normal ou esperada. O objetivo do teste de carga é garantir que o sistema possa lidar com o número esperado de usuários e solicitações.

**Teste de Estresse:** mede o desempenho de um sistema sob uma carga pesada ou inesperada. O objetivo do teste de estresse é identificar os limites do sistema e garantir que ele possa lidar com picos de tráfego ou outras condições adversas.

## Relatório

```txt

```

O relatório gerado pelo k6 contém uma variedade de métricas, incluindo:
 - Tempo de resposta
 - Taxa de transferência
 - Taxa de erro
 - Utilização de recursos

Estas métricas podem ser usadas para avaliar o desempenho do sistema e identificar quaisquer gargalos ou problemas.

## Conclusão
Neste exercício, aprendemos como usar o k6 para realizar testes de carga em um sistema. Também aprendemos sobre os conceitos de teste de carga e teste de estresse.

O k6 é uma ferramenta poderosa que pode ser usada para avaliar o desempenho de um sistema e identificar quaisquer gargalos ou problemas. Os testes de carga e estresse são essenciais para garantir o desempenho e a confiabilidade de um sistema.
