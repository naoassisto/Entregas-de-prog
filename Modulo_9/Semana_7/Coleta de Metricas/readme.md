
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
A aplicação utiliza .NET 6/ASP.NET Core como base, com OpenTelemetry .NET para observabilidade. Prometheus é usado para coleta de métricas e Swagger (Swashbuckle.AspNetCore) é integrado para documentação e teste de API.
Etapas de Configuração
A configuração da aplicação envolveu a criação de um novo projeto ASP.NET Core Web API, adicionando pacotes OpenTelemetry, definindo métricas e rastreamento personalizados e configurando o OpenTelemetry para instrumentação e exportadores ASP.NET Core.
Conclusão
Esta aplicação .NET Web API demonstra como integrar o OpenTelemetry para observabilidade aprimorada, demonstrando métricas personalizadas, rastreamento e configurações de exportador. Serve como um exemplo fundamental para desenvolvedores que desejam implementar soluções de observabilidade semelhantes em seus projetos.

