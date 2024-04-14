from PIL import Image
from streamlit_extras.app_logo import add_logo
import streamlit as st


# Load the image for the page icon
page_icon_image = Image.open('streamlit/images/logo.jpg')

# Configure Streamlit page settings
st.set_page_config(layout="wide", page_title="EDA", page_icon=page_icon_image)

add_logo('streamlit/images/logo.jpg')

# Sidebar header
st.sidebar.header("Exploratory data analysis")

# Main title
st.title("Exploratory data analysis")

# Load your images
image2 = Image.open('streamlit/images/EDA/sales_vs_return_pct.png')
image1 = Image.open('streamlit/images/EDA/eda_returns_per_shop.png')
image3 = Image.open('streamlit/images/EDA/sales_vs_return_pct_per_brand.png')
image4 = Image.open('streamlit/images/EDA/sales_vs_return_pct_per_product.png')
image5 = Image.open('streamlit/images/EDA/price_cat_vs_ret_pct.png')

st.subheader("Sales vs Return Percentage")
st.image(image1, caption='Image 1', use_column_width=True)
st.markdown("This graph shows the percentage returned versus the amount of unique customer IDs. It shows that there are much more physical stores than webshops. One webshop has much more customers than all other stores. Return rates for physical stores  are much lower than for webshops.")

st.subheader("Sales vs Return Percentage per Shop")
st.image(image2, caption='Image 2', use_column_width=True)
st.markdown("Data is grouped by shop. The x-axis is log_scaled for a better overview of the sales amounts. The x-axis shows the sales amount and the y-axis shows the return percentage. The size of the dots represents the number of unique shops where the customer bought products. The color of the dots represents the type of store. The graph shows that the return percentage is higher for webshops than for physical stores. The return percentage is higher for stores with a lower sales amount.")

st.subheader("Sales vs Return Percentage per Brand")
st.image(image3, caption='Image 3', use_column_width=True)
st.markdown("Sales are grouped per brand. The x-axis is log_scaled for a better overview of the sales amounts. The x-axis shows the sales amount and the y-axis shows the return percentage. The size of the dots represents the number of unique customer IDs. The color of the dots represents the type of store. Brands with more sales have lower return percentages. There is a much bigger selection of brands in physical stores than webshops")

st.subheader("Sales vs Return Percentage per Product")
st.image(image4, caption='Image 4', use_column_width=True)
st.markdown("Sales are grouped per product. The x-axis is log_scaled for a better overview of the sales amounts. The x-axis shows the sales amount and the y-axis shows the return percentage. The size of the dots represents the number of shops where the product is available. The color of the dots represents the type of store. Products with more sales have lower return percentages. The few brands on webshops have a large amount of product variation.")

st.subheader("Price Category vs Return Percentage per Product")
st.image(image5, caption='Image 5', use_column_width=True)
st.markdown("The prices are divided into 5 categories. The x-axis shows the price category and the y-axis shows the return percentage. The size of the dots represents the number of unique customer IDs. The color of the dots represents the type of store. The return percentage is higher for products in the higher price categories.")  