
## Visão Geral
Este documento fornece um relato detalhado do desenvolvimento e configuração de uma aplicação .NET Web API com observabilidade integrada através do OpenTelemetry. Inclui a funcionalidade principal, as alterações realizadas, as tecnologias utilizadas e as necessidades específicas atendidas por essas alterações.
## Alterações Realizadas

### Integração do OpenTelemetry
Introduziu o OpenTelemetry na aplicação para permitir a coleta de métricas e rastreamentos para melhor observabilidade.
```c#
builder.Services.AddOpenTelemetry()
    .ConfigureResource(resourceBuilder => 
        resourceBuilder.AddService("MyApp"))
    .WithMetrics(metricsBuilder =>
    {
        metricsBuilder.AddAspNetCoreInstrumentation(); 
        metricsBuilder.AddConsoleExporter();
    })
    .WithTracing(tracingBuilder =>
    {
        tracingBuilder.AddAspNetCoreInstrumentation();
        tracingBuilder.AddConsoleExporter();
    });
```

### Métricas e Rastreamento Personalizados
Implementou métricas personalizadas para contar saudações e um ActivitySource personalizado para rastrear atividades de saudação.

```C#
var greeterMeter = new Meter("OtPrGrYa.Example", "1.0.0");
var countGreetings = greeterMeter.CreateCounter<int>("greetings.count", description: "Conta o número de saudações");
```

### Exemplo de Rastreamento Personalizado:
```C#
var greeterActivitySource = new ActivitySource("OtPrGrJa.Example");
Use code with caution.
````

### Configuração do Exportador

Configurou exportadores de console e Prometheus para métricas e configurou o exportador OTLP para rastreamentos com base na disponibilidade de um endpoint.

```c#
otel.WithMetrics(metrics => metrics
    .AddAspNetCoreInstrumentation()
    .AddMeter(greeterMeter.Name)
    .AddPrometheusExporter());
```

## Endpoint da API
Criou um endpoint de API mínimo (/) para enviar uma saudação, incrementar a métrica personalizada e criar um rastreamento.
```C#
app.MapGet("/", SendGreeting);

async Task<String> SendGreeting(ILogger<Program> logger)
{
    using var activity = greeterActivitySource.StartActivity("GreeterActivity");
    logger.LogInformation("Enviando saudação");
    countGreetings.Add(1);
    activity?.SetTag("greeting", "Olá Mundo!");
    return "Olá Mundo!";
}
```
## Necessidades
A principal necessidade era aprimorar a observabilidade da aplicação por meio de métricas e rastreamentos para melhores recursos de monitoramento e depuração. Além disso, a implementação de diagnósticos foi crucial para entender o comportamento da aplicação em várias condições.

## Tecnologias Utilizadas
 - A aplicação utiliza .NET 6/ASP.NET Core como base, com OpenTelemetry .NET para observabilidade. Prometheus é usado para coleta de métricas e Swagger (Swashbuckle.AspNetCore) é integrado para documentação e teste de API.
Etapas de Configuração
 - A configuração da aplicação envolveu a criação de um novo projeto ASP.NET Core Web API, adicionando pacotes OpenTelemetry, definindo métricas e rastreamento personalizados e configurando o OpenTelemetry para instrumentação e exportadores ASP.NET Core.
Conclusão
 - Esta aplicação .NET Web API demonstra como integrar o OpenTelemetry para observabilidade aprimorada, demonstrando métricas personalizadas, rastreamento e configurações de exportador. Serve como um exemplo fundamental para desenvolvedores que desejam implementar soluções de observabilidade semelhantes em seus projetos.

# Relatório de Métricas de Telemetria

## Resumo Geral

Este relatório documenta as métricas coletadas de uma aplicação .NET executando localmente. As métricas são derivadas do SDK OpenTelemetry (versão 1.0.8-beta.1) e capturam detalhes de atividades de telemetria como conexões ativas, solicitações HTTP e tentativas de roteamento.

## Atividades Registradas

Durante o período de observação, várias atividades foram registradas:

- `Greeting` com um `Duration` de 30 milissegundos.
- `Server` atendendo a uma solicitação HTTP GET, também com `Duration` na casa dos milissegundos.

Ambas as atividades indicam resposta rápida e processamento eficiente sem atrasos significativos.

## Métricas do Servidor

### Conexões

- **Conexões Ativas**: Houve um total de 2 conexões ativas no momento da coleta de métricas, o que sugere uma carga leve sobre o servidor.

### Solicitações HTTP

- **Solicitações Ativas**: A aplicação processou várias solicitações HTTP GET com código de status `200`, indicando sucesso nas respostas.
- **Duração das Solicitações**: A duração das solicitações se manteve estável, com valores mínimos e máximos muito próximos, demonstrando consistência na resposta do servidor.

### Métricas de Roteamento

- **Tentativas de Roteamento**: Houve uma tentativa de roteamento bem-sucedida, sem falhas registradas.

## Observações de Telemetria

O sistema parece estar operando dentro de parâmetros normais, sem indicações de falha ou performance degradada. As respostas são rápidas e não há acumulação de conexões ou solicitações.

![Imgur](https://imgur.com/8sHES96.png)
[Imgur](https://imgur.com/9EsZwDa.png)
[Imgur](https://imgur.com/6JdwE2A.png)
[Imgur](https://imgur.com/AB9boPe.png)
[Imgur](https://imgur.com/HIpFppE.png)


