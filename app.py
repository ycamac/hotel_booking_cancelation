import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
    page_title="Hotelligence - Hotel Booking Cancellation Predictor",
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
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'username' not in st.session_state:
    st.session_state.username = None

# Main app
def main():
    """Main application function"""
    # Initialize page state
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    
    # Check authentication
    if not st.session_state.authenticated:
        login_page()
        return
    
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

if __name__ == "__main__":
    main() 