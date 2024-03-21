using System.Diagnostics;
using System.Diagnostics.Metrics;
using OpenTelemetry.Logs;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
// using OpenTelemetry.Exporter.Prometheus.AspNetCore;

var builder = WebApplication.CreateBuilder(args);

// Configure basic OpenTelemetry
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

// Custom metrics and activity source
var greeterMeter = new Meter("OtPrGrYa.Example", "1.0.0");
var countGreetings = greeterMeter.CreateCounter<int>("greetings.count", description: "Counts the number of greetings");
var greeterActivitySource = new ActivitySource("OtPrGrJa.Example");

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configure advanced OpenTelemetry
var tracingOtlpEndpoint = builder.Configuration["OTLP_ENDPOINT_URL"];
var otel = builder.Services.AddOpenTelemetry();

otel.ConfigureResource(resource => resource
    .AddService(serviceName: builder.Environment.ApplicationName));

otel.WithMetrics(metrics => metrics
    .AddAspNetCoreInstrumentation()
    .AddMeter(greeterMeter.Name)
    .AddMeter("Microsoft.AspNetCore.Hosting")
    .AddMeter("Microsoft.AspNetCore.Server.Kestrel")
    .AddPrometheusExporter());

otel.WithTracing(tracing =>
{
    tracing.AddAspNetCoreInstrumentation();
    tracing.AddHttpClientInstrumentation();
    tracing.AddSource(greeterActivitySource.Name);
    if (tracingOtlpEndpoint != null)
    {
        tracing.AddOtlpExporter(otlpOptions =>
        {
            otlpOptions.Endpoint = new Uri(tracingOtlpEndpoint);
        });
    }
    else
    {
        tracing.AddConsoleExporter();
    }
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapPrometheusScrapingEndpoint();

app.MapGet("/", SendGreeting);

async Task<String> SendGreeting(ILogger<Program> logger)
{
    using var activity = greeterActivitySource.StartActivity("GreeterActivity");

    logger.LogInformation("Sending greeting");

    countGreetings.Add(1);

    activity?.SetTag("greeting", "Hello World!");

    return "Hello World!";
}

app.Run();