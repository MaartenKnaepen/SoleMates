import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.app_logo import add_logo


# Load the image for the page icon
page_icon_image = Image.open('streamlit/images/logo.jpg')


# Configure Streamlit page settings
st.set_page_config(page_title="Positive Recall Model", page_icon=page_icon_image)

add_logo('streamlit/images/logo.jpg', 20)

# Sidebar header
st.sidebar.header("Positive Recall Model")

# Load your images and data
image1 = Image.open('streamlit/images/pos_recall/FI_pos_recall.png')
image2 = Image.open('streamlit/images/pos_recall/pos_recall_roc_test.png')
image3 = Image.open('streamlit/images/pos_recall/pos_recall_lift_test.png')
image4 = Image.open('streamlit/images/pos_recall/pos_recall_roc_val.png')
image5 = Image.open('streamlit/images/pos_recall/pos_recall_lift_val.png')

# Classification report data
classification_report_data = {
    'Class': ['0', '1', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.99, 0.19, None, 0.59, 0.96],
    'Recall': [0.86, 0.81, None, 0.84, 0.86],
    'F1-score': [0.92, 0.31, None, 0.62, 0.90],
    'Support': [270609, 10974, 281583, 281583, 281583]
}

# Create DataFrame
balanced_test = pd.DataFrame(classification_report_data)


classification_report_data2 = {
    'Class': ['0', '1', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.99, 0.23, None, 0.61, 0.92],
    'Recall': [0.67, 0.96, None, 0.82, 0.69],
    'F1-score': [0.80, 0.37, None, 0.58, 0.76],
    'Support': [319873, 32105, 351978, 351978, 351978]
}

# Create DataFrame
balanced_val = pd.DataFrame(classification_report_data2)

# Display the data
st.title("Positive Recall Model")

st.write('The dataset is imbalanced because the number of not returned items is much bigger than the number of returned items. To counteract this, the model was trained on dataset with downsampled unreturned items to teach the model to better identify the minority class (returned items).')
st.write('After, the model was validated on an unseen part of the original, imbalanced test set to get a more realistic performance evaluation.')
st.write('The models were selected based on the best performance on the validation set.')

st.subheader("Classification report (Test Set)")
st.table(balanced_test)
st.write("Recall measures the ability of the model to correctly identify all positive instances out of all actual positive instances.")
st.write("In this classification report, the recall for class 1 is 0.81. This indicates that the model is capturing around 81% of the actual positive instances for class 1. While the recall for class 1 is relatively high, it's important to note that the precision for class 1 is low (0.19), suggesting that there are many false positives. Improving precision while maintaining high recall would be crucial for class 1 predictions, as it indicates correctly identifying positive instances while minimizing false positives.")

st.subheader("Feature Importance")
st.image(image1, caption='Image 1', use_column_width=True)
st.markdown("The feature importance plot shows the relative importance of each feature in the model. The higher the value, the more important the feature is in predicting the target variable. ")

st.write("In this case, the most important features are 'Webshop', 'SaleDocumentNumber', 'ModelGroup', and 'CustomerID'. This suggests that these features have a significant impact on the model's predictions.")
st.subheader("ROC Curve (Test Set)")
st.image(image2, caption='Image 2', use_column_width=True)
st.markdown("The ROC curve shows the trade-off between the true positive rate (sensitivity) and the false positive rate (1 - specificity) for different classification thresholds. The area under the ROC curve (AUC) is a measure of the model's ability to distinguish between the two classes. A higher AUC indicates better performance. In this case, the AUC is 0.84, which suggests that the model is as good as the validated balanced model at distinguishing between returned and unreturned items.")

st.subheader("Lift Curve (Test Set)")
st.image(image3, caption='Image 3', use_column_width=True)
st.write("The Lift Curve shows the ratio of the model's performance to a random model. The x-axis shows the percentage of the dataset, and the y-axis shows the ratio of the model's performance to a random model. The higher the curve, the better the model's performance. In this case, the model performs better than a random model, especially for the top 20% of the dataset.")

st.subheader("Classification report (Validation Set)")
st.table(balanced_val)
st.write("Recall measures the ability of the model to correctly identify all positive instances out of all actual positive instances.")
st.write("In this classification report, the recall for class 1 is relatively high at 0.96. This indicates that the model is effectively capturing a high percentage of true positives for class 1. However, it's important to note that the precision for class 1 is low (0.23), suggesting that there may be many false positives. While the recall for class 1 is high, improvements in precision would be beneficial to reduce false positives and enhance the overall performance of the model.")

st.subheader("ROC Curve (Validation Set)")
st.image(image4, caption='Image 4', use_column_width=True)
st.markdown("The ROC curve shows the trade-off between the true positive rate (sensitivity) and the false positive rate (1 - specificity) for different classification thresholds. The area under the ROC curve (AUC) is a measure of the model's ability to distinguish between the two classes. A higher AUC indicates better performance. In this case, the AUC is 0.83, which suggests that the model is good at distinguishing between returned and unreturned items.")

st.subheader("Lift Curve (Validation Set)")
st.image(image5, caption='Image 5', use_column_width=True)
st.markdown("The Lift Curve shows the ratio of the model's performance to a random model. The x-axis shows the percentage of the dataset, and the y-axis shows the ratio of the model's performance to a random model. The higher the curve, the better the model's performance. In this case, the model performs better than a random model, especially for the top 40% of the dataset.")  