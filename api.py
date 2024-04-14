from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import xgboost as xgb
import os
import logging

app = FastAPI(
    title="SoleMate ReturnRater",
    description="Predicts the odds that an item with certain characteristics will be returned by the customer",
    version="1.0.0",
)

# Load the models
high_pos = joblib.load("models/XGB_pos_recall_artifacts.joblib")
model_high_pos = high_pos["model"]

balanced = joblib.load("models/XGB_balanced_artifacts.joblib")
model_balanced = balanced["model"]

third_model_path = "models/XGB_artifacts.joblib"
if os.path.exists(third_model_path):
    third = joblib.load(third_model_path)
    model_third = third["model"]

class Item(BaseModel):
    ProductCode: str = Field(..., example='1968361059464632550')
    OriginalSaleAmountInclVAT: float = Field(..., example=99.95)
    CustomerID: str = Field(..., example='-2190786785520839526')
    SaleDocumentNumber: str = Field(..., example='23995792')
    RevenueInclVAT: float = Field(..., example=74.96)
    CostPriceExclVAT: float = Field(..., example=36.534515)
    BrandName: str = Field(..., example='3694837121284491212')
    ModelGroup: str = Field(..., example='3162564956579801398')
    ProductGroup: str = Field(..., example='-453682476182549203')
    Day: int = Field(..., example=30)
    Month: int = Field(..., example=1)
    Weekday: int = Field(..., example=4)
    Webshop: bool = Field(..., example=False)

# Define API tags
tags_metadata = [
    {"name": "predict", "description": "Predict the odds that this item will be returned."},
]

# Assign tags to the entire app
app.openapi_tags = tags_metadata

# Model mapping dictionary
model_mapping = {
    "high_recall": model_high_pos,
    "balanced": model_balanced,
    "third": model_third
}

# Function to convert input data to DMatrix
def convert_to_dmatrix(item: Item):
    data = pd.DataFrame([item.dict()])
    return xgb.DMatrix(data, enable_categorical=True)

@app.get("/")
async def read_root():
    """
    Health check endpoint to ensure the service is alive.
    """
    return {"message": "alive"}

@app.post("/predict/{model_name}", tags=["predict"])
async def predict(item: Item, model_name: str):
    """
    Predicts the odds that an item will be returned based on its characteristics using the selected model.

    **How to use:**
    - Provide input features in the request body.
    - Ensure that the input features are valid.
    - Select the model to use from the available options.

    **Example Usage:**
    ```json
    {
      "ProductCode": "1968361059464632550",
      "OriginalSaleAmountInclVAT": 99.95,
      "CustomerID": "-2190786785520839526",
      "SaleDocumentNumber": "23995792",
      "RevenueInclVAT": 74.96,
      "CostPriceExclVAT": 36.534515,
      "BrandName": "3694837121284491212",
      "ModelGroup": "3162564956579801398",
      "ProductGroup": "-453682476182549203",
      "Day": 30,
      "Month": 1,
      "Weekday": 4,
      "Webshop": false
    }
    ```

    **Responses:**
    - 200 OK: Returns the predicted odds of return.
    - 500 Internal Server Error: If an error occurs during prediction.
    """
    try:
        # Convert input data to DataFrame
        data = pd.DataFrame([item.dict()])

        # Convert specific columns to categorical data type
        categorical_columns = ["ProductCode", "CustomerID", "SaleDocumentNumber", "BrandName", "ModelGroup", "ProductGroup"]
        for col in categorical_columns:
            data[col] = data[col].astype('category')

        # Convert DataFrame to DMatrix
        dmatrix = xgb.DMatrix(data, enable_categorical=True)

        # Select the appropriate model based on model_name
        model = model_mapping[model_name]

        # Make predictions
        prediction = model.predict(dmatrix)

        # Return the prediction
        return {"prediction": float(prediction[0])}

    except KeyError:
        raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found.")

    except Exception as e:
        # Log the error for debugging
        logging.error(f"Prediction error: {e}")
        # Return a 500 error response
        raise HTTPException(status_code=500, detail="An error occurred during prediction.") from e
