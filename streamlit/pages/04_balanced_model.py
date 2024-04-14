import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo


# Load the image for the page icon
page_icon_image = Image.open('streamlit/images/logo.jpg')


# Configure Streamlit page settings
st.set_page_config(page_title="Balanced_Model", page_icon=page_icon_image)

add_logo('streamlit/images/logo.jpg', 20)

# Sidebar header
st.sidebar.header("Balanced_Model")

# Load your images and data
image1 = Image.open('streamlit/images/balanced_model/balanced_FI.png')
image2 = Image.open('streamlit/images/balanced_model/balanced_roc_test.png')
image3 = Image.open('streamlit/images/balanced_model/balanced_lift_test.png')
image4 = Image.open('streamlit/images/balanced_model/balanced_roc_val.png')
image5 = Image.open('streamlit/images/balanced_model/balanced_lift_val.png')

# Classification report data
classification_report_data = {
    'Class': ['0', '1', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.98, 0.33, None, 0.66, 0.92],
    'Recall': [0.84, 0.82, None, 0.83, 0.83],
    'F1-score': [0.90, 0.47, None, 0.69, 0.86],
    'Support': [319873, 32105, 351978, 351978, 351978]
}

# Create DataFrame
balanced_val = pd.DataFrame(classification_report_data)


classification_report_data2 = {
    'Class': ['0', '1', 'accuracy', 'macro avg', 'weighted avg'],
    'Precision': [0.98, 0.35, None, 0.66, 0.95],
    'Recall': [0.96, 0.47, None, 0.71, 0.95],
    'F1-score': [0.97, 0.40, None, 0.68, 0.95],
    'Support': [270702, 10881, 281583, 281583, 281583]
}

# Create DataFrame
balanced_test = pd.DataFrame(classification_report_data2)

# Display the data
st.title("Balanced Model")

st.write('The dataset is imbalanced because the number of not returned items is much bigger than the number of returned items. To counteract this, the model was trained on dataset with downsampled unreturned items to teach the model to better identify the minority class (returned items).')
st.write('After, the model was validated on an unseen part of the original, imbalanced test set to get a more realistic performance evaluation.')
st.write('The models were selected based on the best performance on the validation set.')

st.subheader("Classification report (Test Set)")
st.table(balanced_test)
st.write("Recall measures the ability of the model to correctly identify all positive instances out of all actual positive instances.")
st.write("In this classification report, the recall for class 1 is 0.47. This indicates that the model is capturing around 47% of the actual positive instances for class 1. While it's positive that the model is identifying some positive instances, there is room for improvement as a significant portion of positive instances is still being missed. Improving recall for class 1 may be important depending on the specific context and requirements of the application.")

st.subheader("Feature Importance")
st.image(image1, caption='Image 1', use_column_width=True)
st.markdown("The feature importance plot shows the relative importance of each feature in the model. The higher the value, the more important the feature is in predicting the target variable. ")
st.write("In this case, the most important features are 'Webshop', 'SaleDocumentNumber', 'ModelGroup', and 'CustomerID'. This suggests that these features have a significant impact on the model's predictions.")
st.subheader("ROC Curve (Test Set)")
st.image(image2, caption='Image 2', use_column_width=True)
st.markdown("The ROC curve shows the trade-off between the true positive rate (sensitivity) and the false positive rate (1 - specificity) for different classification thresholds. The area under the ROC curve (AUC) is a measure of the model's ability to distinguish between the two classes. A higher AUC indicates better performance. In this case, the AUC is 0.72, which suggests that the model is decent at distinguishing between returned and unreturned items.")

st.subheader("Lift Curve (Test Set)")
st.image(image3, caption='Image 3', use_column_width=True)
st.write("The Lift Curve shows the ratio of the model's performance to a random model. The x-axis shows the percentage of the dataset, and the y-axis shows the ratio of the model's performance to a random model. The higher the curve, the better the model's performance. In this case, the model performs better than a random model, especially for the top 10% of the dataset.")

st.subheader("Classification report (Validation Set)")
st.table(balanced_val)
st.markdown("Recall measures the ability of the model to correctly identify all positive instances out of all actual positive instances. The recall for class 1 is relatively high at 0.82, indicating that the model is effectively capturing a high percentage of true positives for class 1. This suggests that the model is proficient at identifying instances belonging to class 1, which could be crucial if correctly identifying positive instances is particularly important in the context of the application.")


st.subheader("ROC Curve (Validation Set)")
st.image(image4, caption='Image 4', use_column_width=True)
st.markdown("The ROC curve shows the trade-off between the true positive rate (sensitivity) and the false positive rate (1 - specificity) for different classification thresholds. The area under the ROC curve (AUC) is a measure of the model's ability to distinguish between the two classes. A higher AUC indicates better performance. In this case, the AUC is 0.83, which suggests that the model is good at distinguishing between returned and unreturned items.")

st.subheader("Lift Curve (Validation Set)")
st.image(image5, caption='Image 5', use_column_width=True)
st.markdown("The Lift Curve shows the ratio of the model's performance to a random model. The x-axis shows the percentage of the dataset, and the y-axis shows the ratio of the model's performance to a random model. The higher the curve, the better the model's performance. In this case, the model performs better than a random model, especially for the top 25% of the dataset.")  