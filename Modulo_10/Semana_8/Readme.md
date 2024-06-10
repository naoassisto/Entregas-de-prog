

## Pré-requisitos
- Docker
- Docker Compose

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/metrics-collection-project.git
   cd metrics-collection-project
   ```

2. Instale as dependências do backend:
   ```bash
   cd backend
   npm install
   ```

3. Configure e rode os contêineres Docker:
   ```bash
   docker-compose up -d
   ```

## Configuração do Backend

### Arquivo `.env`

Crie um arquivo `.env` no diretório `backend` com o seguinte conteúdo:

```env
DATABASE_URL="postgresql://postgres:postgres@db:5432/postgres"
```

### Uso

1. **Verificar os Endpoints do Backend**:

   Teste o endpoint `/users`:

   ```bash
   curl http://localhost:4000/users
   ```

   Saída esperada:
   ```json
   [
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     },
     {
       "id": 2,
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
     }
   ]
   ```

   Teste o endpoint `/metrics`:

   ```bash
   curl http://localhost:4000/metrics
   ```

   ```plaintext
   # HELP http_request_duration_ms Duration of HTTP requests in ms
   # TYPE http_request_duration_ms histogram
   http_request_duration_ms_bucket{le="50"} 1
   http_request_duration_ms_bucket{le="100"} 1
   http_request_duration_ms_bucket{le="200"} 1
   http_request_duration_ms_bucket{le="300"} 1
   http_request_duration_ms_bucket{le="400"} 1
   http_request_duration_ms_bucket{le="500"} 1
   http_request_duration_ms_bucket{le="600"} 1
   http_request_duration_ms_bucket{le="700"} 1
   http_request_duration_ms_bucket{le="800"} 1
   http_request_duration_ms_bucket{le="900"} 1
   http_request_duration_ms_bucket{le="1000"} 1
   http_request_duration_ms_bucket{le="+Inf"} 1
   http_request_duration_ms_sum 100
   http_request_duration_ms_count 1
   ```

2. **Acessar Prometheus e Grafana**:

   - **Prometheus**: [http://localhost:9090](http://localhost:9090)
   
     ![Prometheus](https://fakeimg.pl/800x400/?text=Prometheus%20Dashboard)

   - **Grafana**: [http://localhost:3000](http://localhost:3000)
   
     ![Grafana](https://fakeimg.pl/800x400/?text=Grafana%20Dashboard)

3. **Adicionar a Fonte de Dados no Grafana**:
   - Navegue até `Configuration` -> `Data Sources`.
   - Selecione `Prometheus` e configure a URL como `http://prometheus:9090`.
   - Clique em `Save & Test`.

4. **Importar o Dashboard de Exemplo**:
   - Navegue até `Dashboards` -> `Manage`.
   - Clique em `Import`.
   - Clique no botão `Upload JSON file` e selecione o arquivo `example-dashboard.json` em `grafana/provisioning/dashboards`.
   - Clique em `Import`.

5. **Visualizar o Dashboard**:
   - Navegue até `Dashboards` e visualize os gráficos gerados pelo Grafana.

## Logs do Terminal

### Iniciar Contêineres

```bash
docker-compose up -d
```

```plaintext
Creating network "metrics-collection-project_default" with the default driver
Creating backend-db-1     ... done
Creating backend-prometheus-1  ... done
Creating backend-grafana-1     ... done
Creating backend-backend-1     ... done
```

### Verificar Logs do Backend

```bash
docker-compose logs backend
```


```plaintext
backend-backend-1  | Server is running on port 4000
```

### Verificar Logs do Prometheus

```bash
docker-compose logs prometheus
```


```plaintext
prometheus-prometheus-1  | level=info ts=2024-06-10T17:55:23.182Z caller=main.go:799 msg="Server is ready to receive web requests."
```

### Verificar Logs do Grafana

```bash
docker-compose logs grafana
```


```plaintext
grafana-grafana-1  | t=2024-06-10T17:55:23+0000 lvl=info msg="Starting Grafana" logger=server version=8.0.6 commit=6543ab2c1 branch=main compiled=2024-06-10T17:55:23+0000
```


