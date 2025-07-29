import streamlit as st
from utils.model import predict_cancellation
import datetime

def render_booking_predictor():
    st.markdown("# Create Booking")
    st.markdown(
        "<span style='color:gray'>Fill in the guest and booking details. The system will predict the likelihood of cancellation.</span>",
        unsafe_allow_html=True,
    )
    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            hotel_type = st.selectbox("Hotel Type", ["City Hotel", "Resort Hotel"])
            lead_time = st.number_input("Lead Time (days)", min_value=0, max_value=365, value=30)
            adults = st.number_input("Number of Adults", min_value=1, max_value=10, value=2)
            children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
            babies = st.number_input("Number of Babies", min_value=0, max_value=5, value=0)
        with col2:
            arrival_date = st.date_input("Arrival Date", value=datetime.date.today())
            nights = st.number_input("Nights", min_value=1, max_value=30, value=3)
            deposit_type = st.selectbox("Deposit Type", ["No Deposit", "Refundable", "Non Refund"])
            customer_type = st.selectbox("Customer Type", ["Transient", "Contract", "Group", "Transient-Party"])
            special_requests = st.number_input("Special Requests", min_value=0, max_value=5, value=0)
        submitted = st.form_submit_button("Submit Booking", use_container_width=True)
    if submitted:
        pred = predict_cancellation()
        booking = {
            "hotel_type": hotel_type,
            "lead_time": lead_time,
            "adults": adults,
            "children": children,
            "babies": babies,
            "arrival_date": str(arrival_date),
            "nights": nights,
            "deposit_type": deposit_type,
            "customer_type": customer_type,
            "special_requests": special_requests,
            "cancellation_likelihood": pred,
        }
        st.session_state["last_pred"] = pred
        st.session_state["last_booking"] = booking
        if "bookings" not in st.session_state:
            st.session_state["bookings"] = []
        st.session_state["bookings"].append(booking)
        st.success("Booking submitted!")
        st.rerun()
    if "last_pred" in st.session_state and "last_booking" in st.session_state:
        st.markdown("## Cancellation Prediction")
        st.markdown(f"**Likelihood of Cancellation:** <span style='font-size:2rem;color:#e74c3c'>{int(st.session_state['last_pred']*100)}%</span>", unsafe_allow_html=True)
        with st.expander("Show Booking Details"):
            for k, v in st.session_state["last_booking"].items():
                st.write(f"**{k.replace('_', ' ').title()}:** {v}") 