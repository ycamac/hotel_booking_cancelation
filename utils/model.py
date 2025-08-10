import random
import pandas as pd
from datetime import datetime, timedelta
from pycaret.classification import *
from data.country_codes import get_country_code_by_name, get_country_name_by_code, ISO_COUNTRY_CODES

######################################################################################

"""Load the trained model from the specified path."""
def get_model(model_path):
    model = load_model(model_path)
    return model


"""Predict cancellation likelihood for a given booking dataframe."""
def predict_real_cancellation(booking_data, model):
    predictions = model.predict(booking_data)
    return predictions

def get_meal_encoding(meal_type):
    """Convert meal type to numeric encoding"""
    meal_encodings = {
        "BB": 0.0,      # Bed & Breakfast
        "HB": 1.0,      # Half Board
        "FB": 2.0,      # Full Board
        "AI": 3.0,      # All Inclusive
        "Undefined": 4.0
    }
    return meal_encodings.get(meal_type, 4.0)  # Default to Undefined


def get_market_segment_encoding(market_segment):
    """Convert market segment to numeric encoding"""
    segment_encodings = {
        "Direct": 0.0,
        "Online TA": 1.0,
        "Offline TA/TO": 2.0,
        "Complementary": 3.0,
        "Groups": 4.0,
        "Corporate": 5.0,
        "Undefined": 6.0
    }
    return segment_encodings.get(market_segment, 6.0)  # Default to Undefined

def get_distribution_channel_encoding(distribution_channel):
    """Convert distribution channel to numeric encoding"""
    channel_encodings = {
        "Direct": 0.0,
        "TA/TO": 1.0,
        "Undefined": 2.0
    }
    return channel_encodings.get(distribution_channel, 2.0)  # Default to Undefined

def get_room_type_encoding(room_type):
    """Convert room type to numeric encoding"""
    room_encodings = {
        "A": 0.0, "B": 1.0, "C": 2.0, "D": 3.0, "E": 4.0,
        "F": 5.0, "G": 6.0, "H": 7.0, "L": 8.0, "P": 9.0
    }
    return room_encodings.get(room_type, 0.0)  # Default to A

def get_deposit_type_encoding(deposit_type):
    """Convert deposit type to numeric encoding"""
    deposit_encodings = {
        "No Deposit": 0.0,
        "Refundable": 1.0,
        "Non Refundable": 2.0
    }
    return deposit_encodings.get(deposit_type, 0.0)  # Default to No Deposit

def get_customer_type_encoding(customer_type):
    """Convert customer type to numeric encoding"""
    customer_encodings = {
        "Transient": 0.0,
        "Contract": 1.0,
        "Group": 2.0,
        "Transient-Party": 3.0
    }
    return customer_encodings.get(customer_type, 0.0)  # Default to Transient

def prepare_booking_data_for_prediction(hotel_type, check_in, check_out, 
                                       num_adults, num_children, num_babies, special_requests, parking,
                                       meal, country, room_type, deposit_type, customer_type, 
                                       average_daily_rate, assigned_room_type, market_segment, 
                                       distribution_channel, booking_changes, is_repeated_guest, 
                                       previous_cancellations, previous_bookings_not_canceled):
    """
    Prepare booking data from form inputs to match the model's expected format.
    Returns a DataFrame with the same columns as the training data (excluding is_canceled).
    """
    
    # Calculate lead_time automatically based on current date and check-in date
    if check_in:
        check_in_date = check_in if isinstance(check_in, datetime) else datetime.strptime(str(check_in), '%Y-%m-%d')
        current_date = datetime.now().date()
        lead_time = (check_in_date.date() - current_date).days
        lead_time = max(0, lead_time)  # Ensure lead_time is not negative
    else:
        lead_time = 0
    
    # Calculate stays in weekend and week nights
    if check_in and check_out:
        check_in_date = check_in if isinstance(check_in, datetime) else datetime.strptime(str(check_in), '%Y-%m-%d')
        check_out_date = check_out if isinstance(check_out, datetime) else datetime.strptime(str(check_out), '%Y-%m-%d')
        
        total_nights = (check_out_date - check_in_date).days
        weekend_nights = 0
        week_nights = 0
        
        current_date = check_in_date
        for _ in range(total_nights):
            if current_date.weekday() >= 5:  # Saturday (5) or Sunday (6)
                weekend_nights += 1
            else:
                week_nights += 1
            current_date += timedelta(days=1)
    else:
        weekend_nights = 0
        week_nights = 0
    
    # Create the booking data dictionary with all 22 columns
    booking_data = {
        'hotel': hotel_type,
        'lead_time': float(lead_time),
        'stays_in_weekend_nights': float(weekend_nights),
        'stays_in_week_nights': float(week_nights),
        'adults': float(num_adults),
        'children': float(num_children),
        'babies': float(num_babies),
        'meal': meal,
        'country': country,
        'market_segment': market_segment,
        'distribution_channel': distribution_channel,
        'is_repeated_guest': [1.0 if is_repeated_guest == "Yes" else 0.0],
        'previous_cancellations': [float(previous_cancellations)],
        'previous_bookings_not_canceled': float(previous_bookings_not_canceled),
        'reserved_room_type': room_type,
        'assigned_room_type': assigned_room_type,
        'booking_changes': float(booking_changes),
        'deposit_type': deposit_type,
        'customer_type': customer_type,
        'adr': float(average_daily_rate),
        'required_car_parking_spaces': float(parking),
        'total_of_special_requests': float(special_requests)
    }
    
    return pd.DataFrame(booking_data)

######################################################################################

def get_model_metrics():
    return {
        "Accuracy": 0.87,
        "Precision": 0.81,
        "Recall": 0.79,
        "F1 Score": 0.80,
    }

def predict_cancellation():
    return round(random.uniform(0, 1), 2) 