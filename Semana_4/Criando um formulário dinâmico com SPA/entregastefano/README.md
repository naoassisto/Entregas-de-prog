# Entregastefano
# Aplicação Angular de Formulários Dinâmicos


## Tecnologias Utilizadas

- **Angular**: Uma plataforma e framework para a construção de aplicações cliente de página única usando HTML e TypeScript. Angular é usado como o principal framework de desenvolvimento.
- **Módulo de Formulários Angular**: Utilizado para criar e gerenciar formulários no Angular, especificamente Formulários Reativos para cenários mais complexos.
- **RxJS**: Uma biblioteca para programação reativa usando observáveis que facilita a composição de código assíncrono ou baseado em callbacks.
- **Node.js e npm**: Usados para gerenciar dependências do projeto e executar scripts.
- **TypeScript**: A principal linguagem de programação usada, fornecendo definições de tipos estáticos para JavaScript.

## Estrutura do Projeto

O projeto é estruturado em vários componentes chave, com cada um responsável por uma parte da funcionalidade da aplicação:

- `AppComponent`: O componente raiz da aplicação.
- `DynamicFormComponent`: Responsável por renderizar formulários dinâmicos com base em dados de entrada.

### Arquivos Principais

- `app.module.ts`: Define o módulo raiz da aplicação, incluindo declarações e importações necessárias para a execução da aplicação.
- `app.component.ts`: O principal componente da aplicação.
- `dynamic-form.component.ts`: Define a lógica para gerar formulários dinâmicos.
- `app.component.html`: O template principal da aplicação.
- `dynamic-form.component.html`: O template para renderizar formulários dinâmicos.

## Configuração e Instalação

1. Certifique-se de ter o Node.js e npm instalados no seu sistema.
2. Clone o repositório para sua máquina local.
3. Navegue até o diretório do projeto e execute `npm install` para instalar as dependências.
4. Execute `ng serve` para iniciar o servidor de desenvolvimento. A aplicação estará disponível em `http://localhost:4200/`.

## Uso

![Imagem 1](https://i.imgur.com/sjxW4mq.jpg)
![Imagem 2](https://i.imgur.com/7bKbWhb.jpg)


A aplicação gera dinamicamente formulários com base em um conjunto predefinido de perguntas. As perguntas podem ser configuradas no `DynamicFormComponent`, e a aplicação renderizará os campos do formulário de acordo.

