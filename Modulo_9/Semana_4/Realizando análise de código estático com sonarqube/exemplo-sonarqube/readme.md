# Documentação de Análise de Código com SonarQube

## Technologias utilizadas 

- **Docker**: Utilizado para a execução do SonarQube em um ambiente isolado, garantindo que a instalação seja simples e não interfira com o sistema ou com outras aplicações.
  
- **SonarQube**: Uma plataforma de código aberto para realizar análises automáticas de código a fim de detectar bugs, vulnerabilidades de segurança e code smells em seu projeto. É uma ferramenta essencial para garantir a qualidade do código e a segurança da aplicação.
  
- **SonarScanner**: Uma ferramenta de linha de comando específica para a execução de análises de código com SonarQube. Neste caso, foi utilizado o SonarScanner para .NET Core, indicando a integração com projetos desenvolvidos nesta plataforma.
  
- **.NET Core**: Um framework de desenvolvimento de alta performance para a construção de aplicações web e serviços. Foi escolhido como o projeto de exemplo para demonstrar a análise de código, destacando a versatilidade do SonarQube em trabalhar com diversas linguagens de programação e plataformas.

## Conceitos Aprendidos


- **Análise Estática de Código**: A compreensão de como ferramentas como o SonarQube podem examinar o código-fonte sem executá-lo para identificar problemas potenciais.
  
- **Quality Gates**: Aprendizado sobre como definir e usar critérios de qualidade que o código deve atender antes de ser considerado pronto para produção, ajudando a garantir que apenas código de alta qualidade seja entregue.
  
- **Vulnerabilidades de Segurança e Code Smells**: Identificação e compreensão de vulnerabilidades de segurança comuns e maus padrões de código que podem levar a bugs ou problemas de manutenção.
  
- **CI/CD**: Integração com processos de Integração Contínua e Entrega Contínua (CI/CD), utilizando o SonarScanner para automatizar a análise de código como parte do pipeline de desenvolvimento.
  
- **Melhores Práticas de Desenvolvimento**: Reforço da importância de seguir as melhores práticas de desenvolvimento e como a análise de código pode ajudar a identificar desvios dessas práticas.

## Configuração do Ambiente

1. **Instalação do SonarQube e SonarScanner:**
   - SonarQube é executado em um contêiner Docker para facilidade de instalação e isolamento.
   - SonarScanner é uma ferramenta de linha de comando que executa a análise de código.

2. **Preparação do Projeto:**
   - Um projeto de exemplo em .NET Core é utilizado para demonstrar a análise.
     `git clone https://github.com/oktadev/dotnet-sonarqube-example`

   - Inicie o Servidor SonarQube: Use o comando Docker seguinte para iniciar o servidor SonarQube.
   `docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube`

   - Login no SonarQube: Acesse http://localhost:9000 no seu navegador.
   Use o login admin e a senha admin, e será solicitado que você mude a senha.

   - Instale o SonarScanner para .NET Core
   `dotnet tool install --global dotnet-sonarscan

## Processo de Análise

1. **Início da Análise:**
   Rode o comando:
   `dotnet sonarscanner begin /k:"project-key" /d:sonar.login=admin /d:sonar.password=admin`
   
2. **Construção do Projeto:**
   - `dotnet build` é executado para compilar o projeto e coletar informações necessárias para a análise.
     `dotnet build <caminho_para_solucao.sln>`

4. **Finalização da Análise:**
   - Após a construção, a análise é concluída com `dotnet sonarscanner end`.
     `dotnet sonarscanner end /d:sonar.login=admin /d:sonar.password=admin`

## Resultados da Análise

Os resultados da análise são disponibilizados na interface web do SonarQube.

### Dashboard Principal

![Image 1](https://i.imgur.com/JyNqLtr.png)

- **Status do Quality Gate:** Mostra se o código passou pelos critérios de qualidade definidos.
- **Medidas:** Apresenta um resumo das métricas de qualidade do código, incluindo segurança, confiabilidade e manutenibilidade.

### Visão Geral dos Projetos (Screenshot 2)

![Image 2](https://i.imgur.com/7mpHt9X.png)

- **Lista de Projetos:** Exibe todos os projetos analisados e seus status.

### Issues (Screenshot 3)

![Image 3](https://i.imgur.com/HXt39Lr.png)

- **Lista de Problemas:** Detalha os problemas identificados no código, como bugs e code smells.
- **Detalhes dos Problemas:** Fornece informações sobre onde o problema ocorre e sugestões de como resolvê-lo.

### Detalhes de Issues Específicos (Screenshot 4 e 5)

![Image 1](https://i.imgur.com/Iwdt4GE.png)
![Image 2](https://i.imgur.com/qu0SgNo.png)

- **Visão Detalhada:** Oferece uma visão aprofundada de cada problema, localização no código e impacto na qualidade.

### Visão do Código Fonte (Screenshot 6)

![Image 3](https://i.imgur.com/SGaCJSF.png)

- **Código com Problemas Marcados:** Mostra o código fonte com destaques nos trechos onde os problemas foram identificados.

