import streamlit as st

# Import components
from components.styling import load_css
from components.navigations import create_navigation
from components.auth import login_page

st.set_page_config(
    page_title="Hotellingece - Predict your guests\' next move",
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
def initialize_session_state():
    """Initialize session state variables"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    if 'db_path' not in st.session_state:
        st.session_state.db_path = None

# Initialize session state
initialize_session_state()

#################################################################################
# Main function to control the app flow
#################################################################################
def main():
    # Check authentication
    if not st.session_state.authenticated:
        # Ensure we're on login page when not authenticated
        st.session_state.page = "login"
        st.markdown("""
            <div class="header">    
                <div style="padding: 5px 15px;"><b>Hotelligence:</b> Predict your guests' next move</div>
            </div>
            """, unsafe_allow_html=True)
        login_page()

    else:
        # User is authenticated, show navigation
        create_navigation()

    #We include the footer in the main app flow
    st.markdown("""<div class="footer">Copyright © 2025</div>""", unsafe_allow_html=True)
    

if __name__ == "__main__":
    main() 