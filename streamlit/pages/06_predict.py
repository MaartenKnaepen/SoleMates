import streamlit as st
import requests
from pydantic import BaseModel
import os

# Main title
st.title("Predict")

class Item(BaseModel):
    ProductCode: str
    OriginalSaleAmountInclVAT: float
    CustomerID: str
    SaleDocumentNumber: str
    RevenueInclVAT: float
    CostPriceExclVAT: float
    BrandName: str
    ModelGroup: str
    ProductGroup: str
    Day: int
    Month: int
    Weekday: int
    Webshop: bool

# Sidebar header
st.sidebar.header("Select model")
models = ["High Positive Recall Model", "Balanced Model"]
if os.path.exists("models/XGB_artifacts.joblib"):
    models.append("Third Model")
model_name = st.sidebar.selectbox("Model", models)

# Model selection mapping
model_mapping = {
    "High Positive Recall Model": "high_recall",
    "Balanced Model": "balanced",
    "Third Model": "third"
}

# Input form
product_code = st.text_input("Product Code", value='1968361059464632550')
original_sale_amount = st.number_input("Original Sale Amount Incl VAT", value=99.95)
customer_id = st.text_input("Customer ID", value='-2190786785520839526')
sale_document_number = st.text_input("Sale Document Number", value='23995792')
revenue_incl_vat = st.number_input("Revenue Incl VAT", value=74.96)
cost_price_excl_vat = st.number_input("Cost Price Excl VAT", value=36.53)
brand_name = st.text_input("Brand Name", value='3694837121284491212')
model_group = st.text_input("Model Group", value='3162564956579801398')
product_group = st.text_input("Product Group", value='-453682476182549203')
day = st.number_input("Day", value=30)
month = st.number_input("Month", value=1)
weekday = st.number_input("Weekday", value=4)
webshop = st.checkbox("Webshop")

# Predict button
if st.button("Predict"):
    item = Item(
        ProductCode=product_code,
        OriginalSaleAmountInclVAT=original_sale_amount,
        CustomerID=customer_id,
        SaleDocumentNumber=sale_document_number,
        RevenueInclVAT=revenue_incl_vat,
        CostPriceExclVAT=cost_price_excl_vat,
        BrandName=brand_name,
        ModelGroup=model_group,
        ProductGroup=product_group,
        Day=day,
        Month=month,
        Weekday=weekday,
        Webshop=webshop
    )

    # Make a POST request to the FastAPI endpoint with selected model
    response = requests.post(f"http://localhost:8007/predict/{model_mapping[model_name]}", json=item.dict())

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.write(f"The predicted odds that the item will be returned: {prediction:.2%}")
    else:
        st.error("Failed to get prediction from the server.")
