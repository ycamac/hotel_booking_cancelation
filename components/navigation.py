import streamlit as st

def create_navigation():
    """Create the main navigation bar"""
    if not st.session_state.authenticated:
        return
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns([3, 1, 1, 1, 1, 1, 1])
    
    with col1:
        st.markdown("⭐ **HOTELLINGECE**", unsafe_allow_html=True)
    
    with col2:
        if st.button("Home"):
            st.session_state.page = "home"
            st.rerun()
    
    with col3:
        if st.button("Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
    
    with col4:
        if st.button("New Booking"):
            st.session_state.page = "new_booking"
            st.rerun()
    
    with col5:
        if st.button("Bookings"):
            st.session_state.page = "bookings"
            st.rerun()
    
    with col6:
        if st.button("About"):
            st.session_state.page = "about"
            st.rerun()
    
    with col7:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.page = "login"
            st.rerun() 