import streamlit as st
from trainer import Trainer
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import joblib
st.set_option('deprecation.showPyplotGlobalUse', False)

# Function to save uploaded file
def save_uploaded_file(uploaded_file, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

# Streamlit UI
def main():
    st.title("XGBoost Model Trainer")
    st.sidebar.header("Model Configuration")
    
    # Sidebar inputs
    
    valpct = st.sidebar.slider("Validation Data Percentage:", 0.1, 0.9, 0.8)
    train_test_splt = st.sidebar.slider("Train-Test Split:", 0.1, 0.9, 0.2)
    scale_pos_weight = st.sidebar.number_input("Scale Positive Weight:", value=5.85)
    uploaded_file = st.sidebar.file_uploader("Upload Data File (CSV or Parquet)", type=["csv", "parquet"])
    # Check if file is uploaded
    if uploaded_file is not None:
        # Save the uploaded file
        save_uploaded_file(uploaded_file, "streamlit/trainer")

        # Initialize the Trainer object
        trainer = Trainer("streamlit/trainer/" + uploaded_file.name, valpct, train_test_splt, scale_pos_weight)
        
        # Preprocess the data
        st.subheader("Preprocessing Data")
        with st.spinner('Preprocessing data...'):
            X_train, X_test, y_train, y_test, yval, Xval = trainer.preprocess_data()
            st.success('Data preprocessing complete.')

        # Train the model
        st.subheader("Training Model")
        with st.spinner('Training model...'):
            clf = trainer.train_model(X_train, X_test, y_train, y_test)
            st.success('Model trained successfully.')

        # Save the model
        if st.button("Save Model"):
            artifacts = {"model": clf}
            joblib.dump(artifacts, "models/XGB_artifacts.joblib")
            st.write("Model saved successfully")

        # Display ROC curve and confusion matrix for test data
        st.subheader("Test Data Evaluation")
        roc_curve_path = trainer.roc_curve(y_test, clf.predict(X_test))
        st.image(roc_curve_path)
        st.subheader("Confusion Matrix (Test Data)")
        cm_test = confusion_matrix(y_test, clf.predict(X_test))
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm_test, annot=True, cmap='Blues', fmt='g')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix (Test Data)')
        st.pyplot()

        # Display ROC curve and confusion matrix for validation data
        st.subheader("Validation Data Evaluation")
        roc_curve_path_val = trainer.roc_curve(yval, clf.predict(Xval))
        st.image(roc_curve_path_val)
        st.subheader("Confusion Matrix (Validation Data)")
        cm_val = confusion_matrix(yval, clf.predict(Xval))
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm_val, annot=True, cmap='Blues', fmt='g')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix (Validation Data)')
        st.pyplot()

        # Display feature importance
        st.subheader("Feature Importance")
        feature_importance_path = trainer.feature_importance(clf)
        st.image(feature_importance_path)

        # Display lift curve
        st.subheader("Lift Curve")
        lift_curve_path = trainer.plot_lift_curve(yval, clf.predict_proba(Xval)[:,1])
        st.image(lift_curve_path)
    else:
        st.write("Please upload a file.")

if __name__ == "__main__":
    main()
