from sklearn.metrics import accuracy_score, precision_score, recall_score
from prefect import task
import mlflow

@task
def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    return accuracy, precision, recall