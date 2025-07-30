import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64

# Import components
from components.styling import load_css
from components.navigations import create_navigation
from components.auth import login_page

# Page configuration
st.set_page_config(
    page_title="Hotellingece - Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit sidebar and default UI elements
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stApp > div:first-child {display: none !important;}
</style>
""", unsafe_allow_html=True)

# Load custom CSS
load_css()



# Initialize session state

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'username' not in st.session_state:
    st.session_state.username = None

if 'bookings' not in st.session_state:
    st.session_state.bookings = []

# Function to get base64 encoded image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_str = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{b64_str}"

#################################################################################
# Main function to control the app flow
#################################################################################
def main():

    # Initialize page state
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    
    # Check authentication
    if not st.session_state.authenticated:
        st.markdown("""
            <div class="header">    
                <div style="padding: 5px 15px;"><b>Hotelligence:</b> Predict your guests' next move</div>
            </div>
            """, unsafe_allow_html=True)
        login_page()
    else:
        # Check if the page is set to login, and redirect to home if so
        if st.session_state.page == "login":
            st.session_state.page = "home"

        create_navigation()

        # logo_b64 = get_base64_image("images/logo_menu.jpg")

   
    st.markdown("""<div class="footer">Copyright © 2025</div>""", unsafe_allow_html=True)
    

if __name__ == "__main__":
    main() 