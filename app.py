import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64

# Import components
from components.styling import load_css
from components.navigation import create_navigation
from components.auth import login_page

# Import pages
from pages.home_page import home_page
from pages.new_booking_page import new_booking_page
from pages.bookings_page import bookings_page
from pages.dashboard_page import dashboard_page
from pages.about_page import about_page

# Page configuration
st.set_page_config(
    page_title="Hotellingece - Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="wide"
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
# if 'bookings' not in st.session_state:
#     st.session_state.bookings = []

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'username' not in st.session_state:
    st.session_state.username = None

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_str = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{b64_str}"

# Main app
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
        logo_b64 = get_base64_image("images/logo_menu.jpg")
        st.markdown(f"""
            <div class="header">
                <img src="{logo_b64}" alt="Hotelligence Logo" style="width: 80px; object-fit:contain;">
                <div>
                    <a href="#" style="margin-right: 20px; color: #6b7280; text-decoration: none;">New Booking</a>
                    <a href="#" style="margin-right: 20px; color: #6b7280; text-decoration: none;">Bookings</a>
                    <a href="#" style="margin-right: 20px; color: #6b7280; text-decoration: none;">Dashboard</a>
                    <a href="#" style="margin-right: 20px; color: #6b7280; text-decoration: none;">About Us</a>
                    <button class="button" style="margin-right: 20px;">Log Out</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Navigation
        create_navigation()

        # Page routing
        if st.session_state.page == "home":
            home_page()
        elif st.session_state.page == "new_booking":
            new_booking_page()
        elif st.session_state.page == "bookings":
            bookings_page()
        elif st.session_state.page == "dashboard":
            dashboard_page()
        elif st.session_state.page == "about":
            about_page()
        elif st.session_state.page == "login":
            login_page()
   
    st.markdown("""<div class="footer">Copyright © 2025</div>""", unsafe_allow_html=True)
    

if __name__ == "__main__":
    main() 