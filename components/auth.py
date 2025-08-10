import streamlit as st
import time

def login_page():
    """Login page component"""


    st.markdown("""
    <div style="margin-top: 5%; color: #6b7280;">
    </div>
    """, unsafe_allow_html=True) 
    #this container centers the login form
    with st.container():

        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
                
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                st.image("images/hotel_logo.jpg")

                with st.form("login_form"):
                    
                    username = st.text_input("Username", help="Enter your username")
                    password = st.text_input("Password", type="password", help="Enter your password")

                    if st.form_submit_button("Log In", type="primary", use_container_width=True):
                        # Simple authentication (in production, use proper authentication)
                        if username == "admin" and password == "password123":
                            # Clear any existing state and set new authentication
                            st.session_state.authenticated = True
                            st.session_state.username = username
                            st.session_state.page = "home"
                            st.session_state.bookings = []
                            st.success("Login successful!!")
                            time.sleep(1)  # Simulate a delay for better UX
                            st.rerun()
                        else:
                            st.error("Invalid username or password. Try admin/password123")
                
                    # st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("""
                <div style="text-align: center; margin-top: 5px; color: #6b7280;">
                    <small>Demo Credentials: admin / password123</small>
                </div>
                """, unsafe_allow_html=True) 