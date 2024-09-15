from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from prefect import task
import mlflow

@task
def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    with mlflow.start_run():
        modelo = XGBClassifier()
        modelo.fit(X_train, y_train)

        mlflow.log_param("model", "XGBClassifier")
        mlflow.sklearn.log_model(modelo, "modelo")

        return modelo, X_test, y_test