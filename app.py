from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
from prophet import Prophet

app = Flask(__name__)

# Load the dataset
data_path = "data/sales_data.csv"
df = pd.read_csv(data_path)
df.columns = ["ds", "y"]  # Prophet requires 'ds' for date and 'y' for values

# Train the Prophet model and save it
def train_model():
    model = Prophet()
    model.fit(df)
    with open("model/forecasting_model.pkl", "wb") as f:
        pickle.dump(model, f)
train_model()

# Load the trained model
with open("model/forecasting_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input for prediction dates
        input_data = request.json
        future_dates = pd.date_range(
            start=input_data["start_date"],
            end=input_data["end_date"]
        )
        future_df = pd.DataFrame({"ds": future_dates})

        # Make predictions
        forecast = model.predict(future_df)
        forecast_result = forecast[["ds", "yhat"]].to_dict(orient="records")

        return jsonify({"status": "success", "forecast": forecast_result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
