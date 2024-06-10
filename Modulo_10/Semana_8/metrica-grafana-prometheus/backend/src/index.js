const express = require('express');
const { PrismaClient } = require('@prisma/client');
const client = require('prom-client');

const app = express();
const prisma = new PrismaClient();
const collectDefaultMetrics = client.collectDefaultMetrics;

// Collect default metrics
collectDefaultMetrics();

// Create a histogram metric
const httpRequestDurationMicroseconds = new client.Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'code'],
  buckets: [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] // Define your buckets here
});

// Middleware to observe request durations
app.use((req, res, next) => {
  const end = httpRequestDurationMicroseconds.startTimer();
  res.on('finish', () => {
    end({ method: req.method, route: req.route ? req.route.path : req.path, code: res.statusCode });
  });
  next();
});

app.get('/users', async (req, res) => {
  const users = await prisma.user.findMany();
  res.json(users);
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
});

app.listen(4000, () => {
  console.log('Server is running on port 4000');
});
