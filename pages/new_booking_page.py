import streamlit as st
from data.bookings_data import create_new_booking

def new_booking_page():
    """New Booking page component"""
    st.markdown('<h1 class="main-header">New Booking</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Create a new booking and get instant cancellation prediction.</p>', unsafe_allow_html=True)
    
    # Booking form
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            guest_name = st.text_input("Guest Name", help="Enter guest name")
            hotel_type = st.selectbox("Hotel Type", ["Select hotel type", "City Hotel", "Resort Hotel"])
            lead_time = st.number_input("Lead Time (days)", min_value=0, max_value=365, value=30, help="Days between booking and arrival")
            num_adults = st.number_input("Number of Adults", min_value=0, max_value=10, value=2)
            num_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
            num_babies = st.number_input("Number of Babies", min_value=0, max_value=5, value=0)
        
        with col2:
            check_in = st.date_input("Check-in Date")
            check_out = st.date_input("Check-out Date")
            special_requests = st.text_area("Special Requests", help="Any special requirements or requests")
            parking = st.selectbox("Parking Required", ["Select parking requirement", "Yes", "No"])
        
        if st.button("Predict Cancellation", type="primary", use_container_width=True):
            # Create new booking with prediction
            new_booking, prediction_score = create_new_booking(guest_name, hotel_type, check_in, check_out)
            
            st.success(f"Prediction Complete!")
            st.markdown(f"""
            <div class="metric-card">
                <h3>Cancellation Prediction</h3>
                <p><strong>Cancellation Likelihood:</strong> {prediction_score}%</p>
                <div class="prediction-score">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {prediction_score}%"></div>
                    </div>
                    <span>{prediction_score}%</span>
                </div>
                <p style="margin-top: 1rem;">
                    This booking has a {'high' if prediction_score > 70 else 'moderate' if prediction_score > 40 else 'low'} likelihood of cancellation. {'Consider proactive measures.' if prediction_score > 70 else 'Monitor closely.' if prediction_score > 40 else 'No action required at this time.'}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add to bookings
            st.session_state.bookings.append(new_booking)
            
            # Show success message and option to view bookings
            st.success("Booking created successfully!")
            if st.button("View All Bookings"):
                st.session_state.page = "bookings"
                st.rerun() 