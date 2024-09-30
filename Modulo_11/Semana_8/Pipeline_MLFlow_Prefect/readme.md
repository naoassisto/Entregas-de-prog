https://colab.research.google.com/drive/17Txaaim8rm-oPi6-Oa60aUC5QlSMVJdt?usp=sharing


# Execução recomemdada pelo colab 
# Pipeline de Machine Learning com Prefect e MLflow

### Ferramentas Utilizadas

- **Prefect**: Uma ferramenta de orquestração que facilita o gerenciamento de fluxos de trabalho e a execução de tarefas de forma sequencial ou paralela.

- **MLflow**: Plataforma usada para gerenciar o ciclo de vida completo de um experimento de machine learning, incluindo rastreamento de métricas, parâmetros e modelos.

## Estrutura do Pipeline

O pipeline foi estruturado em três etapas principais:

1. **Carregamento de Dados**: Utiliza o dataset Iris, amplamente conhecido, para a tarefa de classificação. Os dados são carregados e divididos em conjuntos de treino e teste.
   
2. **Treinamento do Modelo**: Um modelo de classificação **RandomForest** é treinado nos dados. Durante o treinamento, parâmetros como número de estimadores e profundidade máxima são ajustados.
   
3. **Registro no MLflow**: O modelo treinado, seus parâmetros e métricas (como a acurácia) são registrados no MLflow para que possamos acompanhar e comparar diferentes execuções.



### Execução do Pipeline


 Rode os blocos de codigo
## Resultados

Ao rodar o pipeline, o Prefect orquestra a execução das tarefas. O modelo é treinado com sucesso, e os parâmetros e métricas são registrados no MLflow. A acurácia do modelo, por exemplo, foi registrada como **1.0**, o que indica que o modelo se ajustou perfeitamente ao conjunto de teste (pode ser uma indicação de overfitting, dado o pequeno conjunto de dados).

Você pode ajustar o modelo, aumentar o tamanho do conjunto de dados ou alterar os hiperparâmetros para melhorar a generalização.

### Exemplo de Logs

```
12:31:57.968 | INFO    | Task run 'load_data-0c1' - Concluído com sucesso.
12:32:08.678 | INFO    | Task run 'train_model-e85' - Modelo treinado com acurácia: 1.0
12:32:08.902 | INFO    | Flow run 'yellow-mayfly' - Concluído com sucesso.
```


## Conclusão

Este projeto demonstra como usar **Prefect** e **MLflow** para criar um pipeline de machine learning completo e rastreável. A orquestração de tarefas com Prefect torna o processo organizado e escalável, enquanto o MLflow garante que todas as informações relevantes sobre o treinamento do modelo sejam registradas e comparáveis.

