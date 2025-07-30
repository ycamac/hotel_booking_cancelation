import streamlit as st
import os
import pages as pg

from streamlit_navigation_bar import st_navbar

def create_navigation():

    logo_path = os.path.abspath("images/logo_menu.jpg")
    pages = ["Home", "New Booking", "Bookings", "Dashboard", "About Us", "Logout"]
    styles = {
        "nav": {
            "background-color": "rgb(23, 29, 59)",
            "justify-content": "right",        
            "font-family": "Roboto",
            "display": "flex",
            # "font-family": "Work Sans, Noto Sans, sans-serif",
            "font-size": "13px",
        },
        "img": {
            "padding-right": "14px",
        },
        "div": {        
            "width": "100%",
        },
        "span": {
            "color": "white",
            "padding": "14px",
        },
        "active": {
            "background-color": "white",
            "color": "var(--text-color)",
            "font-weight": "normal",
            "padding": "14px",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
    }

    page = st_navbar(pages, styles=styles, options=options)
        
    if page == "Home":
        st.session_state.page = "home"
        pg.home_page()
    elif page == "New Booking":
        st.session_state.page = "new_booking"
        pg.new_booking_page()
    elif page == "Bookings":
        st.session_state.page = "bookings"
        pg.bookings_page()
    elif page == "Dashboard":
        st.session_state.page = "dashboard"
        pg.dashboard_page()
    elif page == "About Us":
        st.session_state.page = "about"
        pg.about_page()
    elif page == "Logout":
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.page = "login"
        st.rerun()

