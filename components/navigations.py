import streamlit as st
import os
import pages as pg

from streamlit_navigation_bar import st_navbar

def create_navigation():

    logo_path = os.path.abspath("images/logo_menu.svg")
    pages = ["New Booking", "Bookings", "Dashboard", "About Us", "Logout"]
    styles = {
        "nav": {
            "background-color": "rgb(23, 29, 59)",
            "justify-content": "center",   
            "align-items": "center",     
            "font-family": "Roboto",
            "display": "flex",
            # "font-family": "Work Sans, Noto Sans, sans-serif",
            "font-size": "13px",
            "padding-left": "1rem",
            "padding-right": "1rem",
        },
        "img": {
            "margin-left": "0px",
            "margin-right": "800px",
            "height": "45px"
        },
        "div": {        
            "max-width": "100%",
            "width": "100%",
        },
        "span": {
            "color": "white",
            "padding": "15px",
        },
        "active": {
            "background-color": "white",
            "color": "var(--text-color)",
            "font-weight": "normal",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
        "use_padding": False,
    }

    page = st_navbar(pages, styles=styles, logo_path=logo_path, logo_page="home_page", options=options)
        

    if page == "home_page":
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

