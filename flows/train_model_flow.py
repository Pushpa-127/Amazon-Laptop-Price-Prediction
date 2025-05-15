from prefect import flow, task
import pandas as pd
import pickle
import subprocess
from sklearn.linear_model import LinearRegression

@task
def load_data():
    return pd.read_csv("Dataset/laptop_price.csv")

@task
def train_model(df):
    X = df[["Rating", "RAM", "Storage"]]  # adjust to your actual features
    y = df["Price"]
    model = LinearRegression()
    model.fit(X, y)
    return model

@task
def save_model(model):
    with open("Model/model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved!")

@task
def git_commit_push():
    subprocess.run("git config --global user.name 'prefect-bot'", shell=True)
    subprocess.run("git config --global user.email 'bot@example.com'", shell=True)
    subprocess.run("git add Model/model.pkl", shell=True)
    subprocess.run('git commit -m "🤖 Model retrained by Prefect Cloud"', shell=True)
    subprocess.run("git push origin main", shell=True)

@flow(name="Retrain Laptop Price Model")
def ml_training_flow():
    df = load_data()
    model = train_model(df)
    save_model(model)
    git_commit_push()

if __name__ == "__main__":
    ml_training_flow()
