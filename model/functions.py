import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

###############################################################################################################
##Functions for Data Preprocessing
###############################################################################################################

def drop_columns(df, columns):
    df = df.drop(columns, axis=1)
    return df

def handle_missing_values(df):
    missing_cols = df.isna().sum()
    missing_cols = missing_cols[missing_cols > 0]
    for col in missing_cols.index:
        if missing_cols[col] < 50:
            df.dropna(subset=[col],inplace=True)
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df

def get_categorical_columns(df):
    return df.select_dtypes(include=['object', 'category']).columns

def get_feature_columns(df, exclude_col):
    return [cols for cols in df.columns if cols not in exclude_col]

def fit_encoder(df, categorical_cols):
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    encoder.fit(df[categorical_cols])
    return encoder

def transform_with_encoder(df, encoder, categorical_cols):
    encoded = encoder.transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
    df = df.drop(columns=categorical_cols).reset_index(drop=True)
    return pd.concat([df, encoded_df], axis=1)


def fit_minmax_scaler(df, feature_cols):
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[feature_cols] = scaler.fit_transform(df[feature_cols])
    return scaler, df_scaled

def transform_with_scaler(df, feature_cols, scaler):
    df_scaled = df.copy()
    df_scaled[feature_cols] = scaler.transform(df[feature_cols])
    return df_scaled

###############################################################################################################
##Functions for Preparing Booking Data for Prediction
###############################################################################################################

def get_model_metrics():
    model_sum = pd.read_csv("./model/files/model_summary.csv")
    return {
        "Accuracy": model_sum['test_accuracy'][0],
        "Precision": model_sum['test_precision_macro'][0],
        "Recall": model_sum['test_recall_macro'][0],
        "F1 Score": model_sum['test_f1_macro'][0],
    }

def get_model(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def get_encoder(encoder_path):
    with open(encoder_path, "rb") as f:
        encoder = pickle.load(f)
    return encoder

def get_scaler(scaler_path):
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)
    return scaler

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
        'is_repeated_guest': is_repeated_guest,
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


def booking_data_to_dictionary(bookings):
    transformed_data = []
    for booking in bookings:
        transformed_booking = {
            "booking_id": booking["booking_id"],
            "guest_name": booking["guest_name"],
            "check_in": booking["check_in_date"],
            "check_out": booking["check_out_date"],
            "hotel_type": booking["hotel_type"],
            "status": booking["reservation_status"],
            "prediction_score": booking["cancellation_prob"]

            # "lead_time": booking.lead_time,
            # "stays_in_weekend_nights": booking.stays_in_weekend_nights,
            # "stays_in_week_nights": booking.stays_in_week_nights,
            # "adults": booking.adults,
            # "children": booking.children,
            # "babies": booking[7],
            # "meal": booking[8],
            # "country": booking[9],
            # "market_segment": booking[10],
            # "distribution_channel": booking[11],
            # "is_repeated_guest": booking[12],
            # "previous_cancellations": booking[13],
            # "previous_bookings_not_canceled": booking[14],
            # "reserved_room_type": booking[15],
            # "assigned_room_type": booking[16],
            # "booking_changes": booking[17],
            # "deposit_type": booking[18],
            # "customer_type": booking[19],
            # "adr": booking[20],
            # "required_car_parking_spaces": booking[21],
            # "total_of_special_requests": booking[22]
        }
        transformed_data.append(transformed_booking)
    return transformed_data


# booking_date, , , , lead_time, ,
#                     stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, country,
#                     market_segment, distribution_channel, is_repeated_guest, previous_cancellations,
#                     previous_bookings_not_canceled, reserved_room_type, assigned_room_type, booking_changes,
#                     deposit_type, customer_type, adr, required_car_parking_spaces, total_of_special_requests,
#                     , reservation_status_date, 