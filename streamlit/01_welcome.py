import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

# Load the image for the page icon
page_icon_image = Image.open('streamlit/images/logo.jpg')

# Configure Streamlit page settings
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon=page_icon_image,
)

# Hide default Streamlit format for cleaner UI
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Display header text
st.write("#  🎉 Welcome to SoleMates:")
st.write("# Where Data and Footwear Meet! 🎉")

# Display success message in the sidebar
st.sidebar.success("Welcome")

# Display introduction text
st.markdown(
    """
First and foremost, a huge shoutout to [Company Name] for providing me with the platform to strut my stuff and showcase my skills.

At SoleMates, we've curated a user-friendly space where you can step into the realm of product returns prediction with ease. Whether you're a seasoned data guru or just taking your first steps in the data world, we've got something special in store for you!

📊 Exploratory Data Analysis: Take a stroll through our insightful visualizations that unveil the secrets hidden within your data. Uncover trends, patterns, and correlations with just a click!

🤖 Trained Models: We've got not one, but two snazzy models ready to serve you. The first is expertly balanced to predict returns and non-returns alike, ensuring a comprehensive understanding of your data. The second boasts a high recall specifically for returned items, perfect for those all-important predictions.

📁 Data Upload and Prediction: Need to train your own model? Lace up your data and let our system do the heavy lifting. Plus, with our prediction feature, you can anticipate future returns with confidence.

So, whether you're here to crunch numbers or simply explore the possibilities, SoleMates is here to make your journey seamless and enjoyable. Let's put our best foot forward and unlock the potential of your data together!
    """
)

# Define options for navigation
navigation_options = ['Welcome', 'Use case', 'EDA', 'Balanced Model', 'Positive Recall Model', 'Energy', 'Predict!']

# Button to initiate contributing
start_contributing_button = st.button("Get started!")
if start_contributing_button:
    switch_page("Location")
