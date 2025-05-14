from prefect import flow, task
import joblib

@task
def load_dataset():
    df = joblib.load("Model/dataframe.pkl")  # ← Use this!
    return df

@task
def load_model():
    model = joblib.load("Model/pipeline.pkl")
    return model

@task
def make_predictions(model, df):
    predictions = model.predict(df)
    print("✅ Sample Predictions:", predictions[:5])
    return predictions

@flow(name="Laptop Price Prediction Pipeline")
def laptop_price_flow():
    df = load_dataset()
    model = load_model()
    preds = make_predictions(model, df)

if __name__ == "__main__":
    laptop_price_flow()
