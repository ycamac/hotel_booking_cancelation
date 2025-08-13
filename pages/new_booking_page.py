import pandas as pd
import streamlit as st
import model.functions as mf
from data.bookings_data import create_new_booking
from data.country_codes import get_countries_for_selectbox
from datetime import date

def new_booking_page():
    """New Booking page component"""
    st.markdown('<h1 class="main-header">New Booking</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Create a new booking and get instant cancellation prediction.</p>', unsafe_allow_html=True)
    
    # Get countries for selectbox
    countries_options = get_countries_for_selectbox()
    # Booking form
    with st.container():
        col1, col2, col3 = st.columns(3)
        
        # Basic information
        with col1.expander("Basic Information", expanded=True): 
            guest_name = st.text_input("Guest Name", help="Enter guest name")
            num_adults = st.slider("Number of Adults", min_value=0, max_value=10, value=2)
            num_children = st.slider("Number of Children", min_value=0, max_value=10, value=0)
            num_babies = st.slider("Number of Babies", min_value=0, max_value=10, value=0)
            meal = st.selectbox("Meal", ["Select meal", "BB", "FB", "HB", "SC", "Undefined"])
            
            # Country selection with ISO codes
            country_options = [(name, f"{name} ({code})") if code else (name, name) for name, code in countries_options]
            selected_country = st.selectbox(
                "Country", 
                options=[opt[1] for opt in country_options],
                help="Select country with ISO 3166-3 code"
            )
            
            # Extract country code from selection
            country = None
            if selected_country != "Select country":
                # Find the corresponding country code
                for name, code in countries_options:
                    display_name = f"{name} ({code})" if code else name
                    if display_name == selected_country:
                        country = code
                        break
        # Reservation information
        with col2.expander("Reservation Information", expanded=True):
            hotel_type = st.selectbox("Hotel Type", ["Select hotel type", "City Hotel", "Resort Hotel"])
            room_type = st.selectbox("Room Type", ["Select room type", "A", "B", "C", "D", "E", "F", "G", "H", "L", "P"])
            check_in = st.date_input("Check-in Date", value=date.today())
            check_out = st.date_input("Check-out Date", value=check_in)
            special_requests = st.slider("Special Requests", min_value=0, max_value=10, value=0)  
            parking = st.slider("Parking Required", min_value=0, max_value=10, value=0)
            deposit_type = st.selectbox("Deposit Type", ["Select deposit type", "No Deposit", "Refundable", "Non Refundable"], index=1)

        # Additional information    
        with col3.expander("Additional Information", expanded=True):
            assigned_room_type = st.selectbox("Assigned Room Type", ["Select assigned room type", "A", "B", "C", "D", "E", "F", "G", "H", "L", "P"])    
            market_segment = st.selectbox("Market Segment", ["Select market segment", "Direct", "Online TA", "Offline TA/TO", "Complementary", "Groups", "Corporate", "Undefined"], index=1)
            distribution_channel = st.selectbox("Distribution Channel", ["Select distribution channel", "Direct", "TA/TO", "Undefined"], index=1)
            booking_changes = st.slider("Booking Changes", min_value=0, max_value=10, value=0)
            is_repeated_guest = st.selectbox("Is Repeated Guest", ["Select if repeated guest", "Yes", "No"], index=2)
            previous_cancellations = st.slider("Previous Cancellations", min_value=0, max_value=10, value=0)
            previous_bookings_not_canceled = st.slider("Previous Bookings Not Canceled", min_value=0, max_value=10, value=0)
            customer_type = st.selectbox("Customer Type", ["Select customer type", "Transient", "Contract", "Group", "Transient-Party"], index=1)
            average_daily_rate = st.number_input("Average Daily Rate", min_value=0, max_value=10000, value=50)

        # Prediction section
        if st.button("Predict Cancellation", type="primary", use_container_width=True):
            # Validate form inputs
            if (guest_name and hotel_type != "Select hotel type" and 
                check_in and check_out and parking != "Select parking requirement" and
                meal != "Select meal" and country is not None and
                room_type != "Select room type" and deposit_type != "Select deposit type" and
                customer_type != "Select customer type" and assigned_room_type != "Select assigned room type" and
                market_segment != "Select market segment" and distribution_channel != "Select distribution channel" and
                is_repeated_guest != "Select if repeated guest"):
                
                try:
                    # Load the model, encoder and scaler
                    model = mf.get_model("./model/files/rf_model_v3.pkl")
                    encoder = mf.get_encoder("./model/files/catencoder.pkl")
                    scaler = mf.get_scaler("./model/files/fea_scaler.pkl")
                    
                    # Prepare data for prediction
                    booking_df = mf.prepare_booking_data_for_prediction(
                        hotel_type, check_in, check_out,
                        num_adults, num_children, num_babies, special_requests, parking,
                        meal, country, room_type, deposit_type, customer_type,
                        average_daily_rate, assigned_room_type, market_segment,
                        distribution_channel, booking_changes, is_repeated_guest,
                        previous_cancellations, previous_bookings_not_canceled
                    )

                    input_df = pd.DataFrame(booking_df, index=[0])

                    cat_cols = mf.get_categorical_columns(input_df)
                    encoded_df = mf.transform_with_encoder(input_df, encoder, cat_cols)
                    scaled_df = mf.transform_with_scaler(encoded_df, mf.get_feature_columns(encoded_df, exclude_col=[]), scaler)
                    prediction_proba = model.predict_proba(scaled_df)
                    df_prediction_proba = pd.DataFrame(prediction_proba)
                    df_prediction_proba.columns = ['Not canceled', 'Canceled']

                    prediction_score = round(df_prediction_proba['Canceled'].values[0] * 100, 2)
                    
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
                            This booking has a {
                                'high' if prediction_score > 70 else 
                                'moderate' if prediction_score > 40 else 
                                'low'} likelihood of cancellation. {'Consider proactive measures.' if prediction_score > 70 else 'Monitor closely.' if prediction_score > 40 else 'No action required at this time.'}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Create new booking with real prediction
                    new_booking, _ = create_new_booking(guest_name, hotel_type, check_in, check_out)
                    new_booking['prediction_score'] = prediction_score
                    
                    # Add to bookings
                    if 'bookings' not in st.session_state:
                        st.session_state.bookings = []
                    st.session_state.bookings.append(new_booking)
                    
                    # Show success message and option to view bookings
                    st.success("Booking created successfully!")
                    #if st.button("View All Bookings"):
                    #    st.session_state.page = "bookings"
                    #    st.rerun()
                        
                except Exception as e:
                    st.error(f"Error making prediction: {str(e)}")
                    st.info("Please check that all required fields are filled correctly.")
            else:
                st.error("Please fill in all required fields before making a prediction.") 