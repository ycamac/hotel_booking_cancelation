##################################################################################
# The following file is responsible for testing the model
##################################################################################

import functions as mf
import pandas as pd

model = mf.get_model("./model/files/rf_model_v2.pkl")
encoder = mf.get_encoder("./model/files/catencoder.pkl")
scaler = mf.get_scaler("./model/files/fea_scaler.pkl")


hotel_type = "City Hotel"
lead_time = 10
weekend_nights = 2
week_nights = 5
num_adults = 2
num_children = 0
num_babies = 0
meal = "BB"
country = "PER"
market_segment = "Online TA"
distribution_channel = "TA/TO"
is_repeated_guest = "No"
previous_cancellations = 0
previous_bookings_not_canceled = 0
room_type = "A"
assigned_room_type = "A"
booking_changes = 0
deposit_type = "No Deposit"
customer_type = "Transient"
average_daily_rate = 100.0
parking = 1
special_requests = 0

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

input_df = pd.DataFrame(booking_data, index=[0])
print("Input DataFrame for Prediction:")
print(input_df)

cat_cols = mf.get_categorical_columns(input_df)
encoded_df = mf.transform_with_encoder(input_df, encoder, cat_cols)
scaled_df = mf.transform_with_scaler(encoded_df, mf.get_feature_columns(encoded_df, exclude_col=[]), scaler)

print("Input DataFrame Prepared:")
print(scaled_df)

print("Prediction Result:")
print(model.predict_proba(scaled_df))

prediction_proba = model.predict_proba(scaled_df)
df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Not canceled', 'Canceled']

print(round(df_prediction_proba['Not canceled'].values[0] * 100,2))  # Print the non-cancellation probability as a percentage
print(round(df_prediction_proba['Canceled'].values[0] * 100,2))  # Print the cancellation probability as a percentage

