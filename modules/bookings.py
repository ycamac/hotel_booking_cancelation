import streamlit as st
import pandas as pd

def render_bookings():
    st.markdown("# Current Bookings")
    st.markdown("<span style='color:gray'>All bookings submitted in this session.</span>", unsafe_allow_html=True)
    if "bookings" in st.session_state and st.session_state["bookings"]:
        df = pd.DataFrame(st.session_state["bookings"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No bookings yet.") 