# O que é o Cypress e para que serve?

O Cypress é uma ferramenta de teste de front-end moderna projetada para endereçar as complexidades dos aplicativos web modernos. Ele permite que os desenvolvedores e engenheiros de QA configurem, escrevam, executem e depurem testes rapidamente, fácil e confiável. O Cypress é adequado para testar vários tipos de teste, incluindo:


 - Testes de ponta a ponta
 - Testes de componente
 - Testes de integração
 - Testes unitários

Ele pode testar qualquer coisa executada em um navegador.

## Vantagens e desvantagens do Cypress em relação a outras ferramentas de teste

É projetado especificamente para testes de front-end e pode não ser a melhor escolha para testes de back-end ou outros tipos de teste fora do escopo da IU.

Vantagens: 
 - O Cypress opera diretamente no navegador. Permitindo testes mais rápidos, confiáveis e consistentes.
 - O Cypress espera automaticamente por comandos e asserções, eliminando a necessidade de esperas explícitas.
 - Ele fornece ferramentas de depuração avançadas que podem ser integradas a ferramentas de dev conhecidas.
 - Permite controlar, substituir e testar casos extremos facilmente, sem envolver o servidor.

 Desvantagens:
- Limitado aos navegadores Chrome, Firefox, Edge e Electron, podendo não abranger todos os navegadores do público.
- Focado em testes de front-end, não sendo ideal para testes de back-end ou fora do escopo da UI.

Embora suporte testes nos navegadores Chrome, Firefox, Edge e Electron, pode não cobrir todos os navegadores usados por um público diverso.*

## Arquitetura do Cypress
*A arquitetura do Cypress é fundamentalmente diferente das ferramentas de teste tradicionais.*

Ele é executado dentro do navegador, ao lado do aplicativo em teste, fornecendo controle direto sobre o DOM, eventos, armazenamento, etc. Isso elimina a necessidade de drivers ou servidores intermediários, resultando em uma execução de teste mais rápida e direta.
Principais componentes incluem:

- **Cypress Runner**: Carrega o aplicativo no navegador e injeta o código do Cypress.

- **Recurso do Navegador**: Oferece acesso ao DOM, eventos e mais.

- **Espelho do DOM**: Representação em tempo real do DOM para monitoramento eficiente.

- **Kernel do Cypress**: Núcleo responsável por executar comandos e asserções.

- **Plugins**: Extendem a funcionalidade do Cypress, permitindo adicionar suporte a navegadores adicionais, integrar com outras ferramentas ou criar comandos customizados.


### Seletores de elementos no Cypress

O Cypress usa seletores de elementos para interagir com os elementos da IU de um aplicativo. Esses seletores podem ser seletores CSS, como IDs, classes ou atributos específicos dos elementos. Exemplo: 
 - `cy.get()`
 - `cy.find()`
 - `cy.contains()`.
# Comandos e Asseções no Cypress

Os comandos no Cypress facilitam a interação com o aplicativo, possibilitando ações como clicar em botões, digitar em campos de entrada e navegar por páginas. As asserções verificam se a interface do usuário (UI) está no estado esperado após essas ações, com uma gama de asserções para verificar propriedades como visibilidade, conteúdo, atributos, e mais.

## Preparação, Execução e Verificação de Testes no Cypress

### Preparação
- Instale o Cypress e configure seu ambiente de teste.
- Crie arquivos de teste na pasta `cypress/integration`.

### Execução
- Utilize seletores de elementos para identificar componentes da UI a serem testados.
- Escreva comandos para interagir com esses elementos e asserções para verificar o estado do aplicativo.
- Execute os testes usando o Cypress Test Runner, observando a execução em tempo real e integrando-os à linha de comando para CI/CD.

### Verificação
- Analise os resultados no Dashboard do Cypress.
- Utilize ferramentas de depuração para investigar falhas.

## Estruturando Testes Eficientemente no Cypress

Para maximizar a eficiência dos testes no Cypress, siga estas práticas recomendadas:
- Agrupe testes relacionados em arquivos específicos.
- Utilize os hooks do Cypress para preparar condições iniciais e de limpeza.
- Recorra a funções customizadas e comandos do Cypress para reusar código comum.
- Empregue dados externos para alimentar seus testes, assegurando clareza e descritividade.
