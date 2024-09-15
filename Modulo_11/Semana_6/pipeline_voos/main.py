from prefect import flow
from prefect.server.schemas.schedules import CronSchedule
from src.preprocess import carregar_dados, preprocessar_dados
from src.train import treinar_modelo
from src.evaluate import avaliar_modelo
import mlflow

@flow
def pipeline_voos():
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("previsao_atrasos_voos")

    dados = carregar_dados("data/voos.csv")
    X, y = preprocessar_dados(dados)
    modelo, X_test, y_test = treinar_modelo(X, y)
    accuracy, precision, recall = avaliar_modelo(modelo, X_test, y_test)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    pipeline_voos()

    # Criar e aplicar o deployment
    pipeline_voos.serve(
        name="pipeline_voos_local",
        schedule=CronSchedule(cron="0 0 * * *", timezone="America/Sao_Paulo"),
        work_queue_name="local"
    )

    print("Deployment criado com sucesso. Inicie o servidor Prefect e um agente para executar o fluxo.")