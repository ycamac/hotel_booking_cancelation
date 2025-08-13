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
    return {
        "Accuracy": 0.87,
        "Precision": 0.81,
        "Recall": 0.79,
        "F1 Score": 0.80,
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