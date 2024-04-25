## Documentação para Configuração e Implantação de uma Aplicação Backstage com Docker

### Tecnologias Envolvidas
- **Docker**: Uma plataforma para desenvolver, enviar e executar aplicações dentro de contêineres.
- **Docker Compose**: Uma ferramenta para definir e executar aplicações Docker multi-contêiner.
- **GitHub**: Usado para controle de versão e como serviço de hospedagem de repositório.
- **Node.js**: Um ambiente de execução JavaScript construído sobre o motor JavaScript V8 do Chrome, usado aqui dentro de contêineres Docker para executar o Backstage.
- **PostgreSQL**: Um banco de dados relacional de código aberto, usado aqui para armazenar os dados do Backstage.

### Conceitos Aprendidos
- **Construções Docker Multi-estágio**: Construção eficiente de imagens Docker em múltiplas etapas para minimizar o tamanho final.
- **Rede Docker**: Configurando configurações de rede para conectar vários contêineres, como vincular um contêiner de aplicativo web a um contêiner de banco de dados.
- **Gerenciamento de Segredos no Git**: Compreensão da importância de não empurrar dados sensíveis para o controle de versão e como lidar com tais situações.
- **Controle de Versão com Git**: Gerenciando e versionando código usando Git, e entendendo erros comuns como rejeições de push.

### Guia Passo a Passo

#### Configuração do Dockerfile
O Dockerfile é dividido em três estágios para otimizar o processo de construção e minimizar o tamanho da imagem final:

1. **Estágio Base**: Configura o diretório de trabalho e instala dependências.
   ```Dockerfile
   FROM node:18-bullseye-slim as base
   WORKDIR /app
   COPY package.json yarn.lock ./
   RUN yarn install --frozen-lockfile
   ```

2. **Estágio de Construção**: Compila a aplicação e constrói os arquivos necessários.
   ```Dockerfile
   FROM base as builder
   COPY . .
   RUN yarn tsc
   RUN yarn build
   ```

3. **Estágio de Produção**: Prepara a imagem de produção, copia os arquivos construídos do estágio de construção e define o comando para executar a aplicação.
   ```Dockerfile
   FROM node:18-bullseye-slim as production
   WORKDIR /app
   COPY --from=builder /app/packages/backend/dist /app
   COPY --from=builder /app/app-config.yaml /app
   ENV NODE_ENV production
   EXPOSE 7007
   CMD ["node", "packages/backend", "--config", "app-config.yaml"]
   ```

#### Configuração do Docker Compose
O `docker-compose.yml` orquestra a aplicação Backstage e seu banco de dados PostgreSQL:

```yaml
version: '3.8'
services:
  backstage:
    image: backstage
    environment:
      POSTGRES_HOST: db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: example
    ports:
      - '8009:7007'
  db:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: example
      POSTGRES_DB: backstage
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

### Execução e Testes
1. **Construção da Imagem Docker**: Execute `docker build . -t backstage` para criar a imagem Docker usando o Dockerfile multi-estágio.
![](https://imgur.com/Bc6tysN.png)
   
2. **Iniciar a Aplicação**: Execute `docker-compose up` para iniciar a aplicação juntamente com seu banco de dados usando o Docker Compose. Este comando lê o `docker-compose.yml` e inicia os serviços definidos.
![](https://imgur.com/KkadsBm.png)
   
3. **Acesso à Aplicação**: Com as portas mapeadas como `- '8009:7007'`, a aplicação estará acessível em `http://localhost:8009`.

### Resolvendo Erros Comuns
- **Conflitos de Portas**: Se a porta designada já estiver em uso na máquina host, altere o

primeiro número no mapeamento da porta (`8009` neste caso) para outra porta disponível.
- **Rejeições de Push devido a Segredos**: Se o push para o GitHub for bloqueado devido a segredos encontrados no código(Terraform Cloud / Enterprise API Token), altere os commits para remover ou obscurecer os segredos, ou use variáveis de ambiente para gerenciar informações sensíveis fora do código-fonte.

Este guia oferece uma visão abrangente da configuração de uma aplicação Backstage com Docker, aproveitando práticas modernas de devops e garantindo a gestão segura de dados sensíveis.
