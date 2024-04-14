# SoleMates

## Overview

This project aims to develop a web-based dashboard for predicting return likelihood in e-commerce transactions. The dashboard utilizes machine learning models, particularly XGBoost, to predict whether a customer will return an item after purchase. The predictions are based on various features such as product details, customer information, and transaction data.

## Features

- **Exploratory Data Analysis (EDA)**: Visualizes key insights from the dataset, including sales vs. return percentage, sales distribution per shop, brand, and product, and price category vs. return percentage.
- **Model Training**: Trains multiple models (High Positive Recall Model, Balanced Model, Third Model) using XGBoost with different configurations to optimize prediction accuracy and recall.
- **Model Evaluation**: Evaluates model performance using classification reports, ROC curves, confusion matrices, feature importance plots, and lift curves for both test and validation datasets.
- **Prediction**: Provides a user-friendly interface for users to input transaction details and receive real-time predictions on return likelihood.

## Pages

1. **Home**: Landing page with an overview of the project and its objectives.
2. **EDA**: Exploratory Data Analysis page showcasing visualizations and insights derived from the dataset.
3. **High Positive Recall Model**: Details of the model optimized for high recall, including classification reports, ROC curves, and lift curves.
4. **Balanced Model**: Details of the model trained on a balanced dataset, with performance evaluation and visualizations.
5. **Positive Recall Model**: Similar to the Balanced Model page, but focuses on maximizing recall for positive instances.
6. **Predict**: Prediction page where users can input transaction details and receive return likelihood predictions.
7. **Trainer**: Backend page for model training, evaluation, and saving. It includes the Trainer class for data preprocessing, model training, and evaluation.

## Technologies Used

- **Streamlit**: Web framework for building interactive dashboards with Python.
- **Pandas**: Data manipulation and analysis library.
- **XGBoost**: Machine learning library for gradient boosting algorithms.
- **Pydantic**: Data validation and settings management library.
- **Requests**: HTTP library for making API requests.
- **Matplotlib** and **Seaborn**: Data visualization libraries for creating plots and charts.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory and install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app by executing `streamlit run streamlit/01_welcome.py` in your terminal.
4. Run the FastAPI server for the API by executing `uvicorn api:app --host 0.0.0.0 --port 8007`.
5. Access the dashboard in your web browser at `http://localhost:8501`.

## Models

Due to size limitations, the trained models are not included in the repository. However, they are available upon request. Alternatively, users can refer to the `xgboost.ipynb` notebook for instructions on how to train the models using their own datasets.

## Contributors

- [Maarten Knaepen](https://github.com/MaartenKnaepen)

## License

This project is licensed under the [MIT License](LICENSE).
