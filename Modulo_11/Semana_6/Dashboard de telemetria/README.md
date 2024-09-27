

# **DDashboard de Telemetria ClickHouse**


## **Rodar o dash**


### **Arquivo `.env`**

O arquivo `.env` contém as variáveis de ambiente sensíveis do projeto. Exemplo do arquivo `.env`:

```ini
# .env
CLICKHOUSE_HOST=seu_clickhouse_host
CLICKHOUSE_PORT=8443
CLICKHOUSE_USER=seu_usuario
CLICKHOUSE_PASSWORD=sua_senha
CLICKHOUSE_DB=nome_do_banco_de_dados
```

### **Como rodar o projeto**

1. **Instalar dependências**:
   Antes de rodar o projeto, certifique-se de ter instalado todas as dependências. Você pode fazer isso com o seguinte comando, na raiz do projeto:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar variáveis de ambiente**:
   Certifique-se de que o arquivo `.env` está corretamente configurado com suas variáveis de ambiente (como mostrado acima).

3. **Rodar Controller e Front**
     ```bash
     python3 src/backend/clickhouse_connection.py
     ```

   
     ```bash
     cd src/frontend/ 
     streamlit run dashboard.py.py
     ```

4. **Acessar o projeto**:
   Uma vez que o projeto estiver rodando, ele geralmente estará disponível no endereço:
   ```
   http://localhost:8501
   ```
   (ou outro indicado pelo terminal)


## **Filtro de Dados**
Na barra lateral, você encontra a seção **Filtrar Dados**, que permite selecionar diferentes intervalos de tempo, como:

![](./assets/5.png)

- **Últimas 24 horas**
- **Últimos 7 dias**
- **Últimos 30 dias**



## **Visão Geral das Métricas do Sistema**
Esta seção fornece uma visão detalhada de várias métricas extraídas do sistema, que são essenciais para monitorar o estado do banco de dados.

![](./assets/1.png)
![](./assets/2.png)

### **Uso de Memória (Bytes)**
Essa métrica representa a quantidade de memória atualmente sendo usada pelo sistema ClickHouse, em bytes. O uso de memória é crucial, pois um sistema que consome muita memória pode afetar a estabilidade e o desempenho geral. Monitorar o uso de memória permite prever gargalos antes que ocorram, garantindo que o sistema não exceda sua capacidade.


![](./assets/3.png)

### **Threads de Execução Ativas**
Essa métrica mede o número de threads (linhas de execução) ativas no sistema. Esse dado é fundamental para entender como o sistema distribui o trabalho. Muitas threads ativas podem indicar que o sistema está sob alta carga de processamento, o que pode ser um sinal de sobrecarga.

![](./assets/3.png)

### **Conexões TCP Ativas**
Essa métrica monitora o número de conexões TCP em uso no sistema. As conexões TCP são essenciais para a comunicação de rede. Um alto número de conexões pode indicar uma demanda maior por recursos de rede, enquanto um número muito baixo pode sugerir problemas de comunicação entre servidores.

![](./assets/4.png)

## **Gráficos de Desempenho**

### **Uso de Memória e Threads Ativas**
Na aba **Memória e Threads**, você encontra um gráfico que visualiza duas métricas importantes: **Uso de Memória** e **Threads de Execução Ativas**. Esse gráfico ajuda a comparar o uso de memória com o número de threads ativas. Um aumento simultâneo em ambas as métricas pode indicar um aumento na carga do sistema, enquanto a redução de uma métrica e o aumento da outra podem indicar um uso ineficiente dos recursos.

### **Conexões TCP Ativas**
Na aba **Conexões TCP**, o gráfico de barras exibe o número de **Conexões TCP Ativas** no sistema. Monitorar essas conexões é fundamental para garantir que o sistema está funcionando corretamente em termos de comunicação de rede. Picos ou quedas nas conexões podem indicar problemas de conectividade ou sobrecarga na rede.


## **Análise e Insights**
### **Desempenho do Sistema**
Acompanhar o uso de memória, threads de execução e conexões TCP é essencial para identificar gargalos ou sobrecargas no sistema. Isso garante que o ClickHouse funcione de maneira eficiente, sem sobrecarregar seus recursos.

### **Conectividade**
As conexões TCP fornecem insights sobre o uso da rede e as interações entre os componentes do sistema. Ao monitorar essas conexões, é possível antecipar problemas de rede ou falhas de comunicação.

### **Otimização de Consultas**
O número de threads ativas oferece uma boa visão do desempenho das consultas. Um grande número de threads pode indicar que muitas consultas estão sendo processadas ao mesmo tempo, o que pode sobrecarregar o sistema. Identificar esses picos é crucial para otimizar o desempenho geral.

