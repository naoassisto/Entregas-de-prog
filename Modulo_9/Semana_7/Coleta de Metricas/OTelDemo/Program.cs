using System.Diagnostics;
using System.Diagnostics.Metrics;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using OpenTelemetry.Metrics;
using System;

var builder = WebApplication.CreateBuilder(args);

var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

var tracingOtlpEndpoint = builder.Configuration["OTLP_ENDPOINT_URL"];

// Custom metrics for the application
var greeterMeter = new Meter("OtPrGrYa.Example", "1.0.0");
var countGreetings = greeterMeter.CreateCounter<int>("greetings.count", description: "Counts the number of greetings");

// Custom ActivitySource for the application
var greeterActivitySource = new ActivitySource("OtPrGrYa.Example");

// Add services to the container.
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configure OpenTelemetry Tracing
builder.Services.AddOpenTelemetryTracing(tracerProviderBuilder =>
{
    tracerProviderBuilder
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddSource(greeterActivitySource.Name)
        .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService(builder.Environment.ApplicationName))
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri(tracingOtlpEndpoint);
        });
});

// Configure OpenTelemetry Metrics
builder.Services.AddOpenTelemetryMetrics(metricsBuilder =>
{
    metricsBuilder
        .AddAspNetCoreInstrumentation()
        .AddMeter(greeterMeter.Name)
        .AddPrometheusExporter();
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGet("/weatherforecast", () =>
{
    var forecast = Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast(
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]))
        .ToArray();
    return forecast;
}).WithName("GetWeatherForecast").WithOpenApi();

app.MapGet("/", SendGreeting);

app.Run();

string SendGreeting(ILogger<Program> logger)
{
    // Create a new Activity scoped to the method
    using var activity = greeterActivitySource.StartActivity("GreeterActivity");

    // Log a message
    logger.LogInformation("Sending greeting");

    // Increment the custom counter
    countGreetings.Add(1);

    // Add a tag to the Activity
    activity?.SetTag("greeting", "Hello World!");

    return "Hello World!";
}

record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
