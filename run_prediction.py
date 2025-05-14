# run_prediction.py
import pandas as pd
import joblib

# Load test data (or any predefined data)
df = pd.read_csv("Dataset/laptop_data.csv")[:10]  # Example test data

# Load model
model = joblib.load("Model/pipeline.pkl")

# Make predictions
df["PredictedPrice"] = model.predict(df)

# Save to output file
df.to_csv("predictions_output.csv", index=False)
print("✅ Predictions updated.")
