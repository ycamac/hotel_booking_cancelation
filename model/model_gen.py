##################################################################################
# The following file is responsible for generating the model, encoder, and scaler
##################################################################################


import pandas as pd
import pickle
import functions as mf
import skops.io as sio

from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('./model/files/hotel_bookings.csv')

# Preprocess the data
columns_to_drop = ['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month', 'arrival_date_week_number', 'reservation_status_date', 'company', 'agent', 'days_in_waiting_list', 'reservation_status']
prepared_data = mf.drop_columns(data, columns_to_drop)
prepared_data = mf.handle_missing_values(prepared_data)

# Get the categorical columns
categorical_cols = mf.get_categorical_columns(prepared_data)

# Encode categorical features
encoder = mf.fit_encoder(prepared_data, categorical_cols)
prepared_data = mf.transform_with_encoder(prepared_data, encoder, categorical_cols)

# Get the columns to scale
scaling_cols = mf.get_feature_columns(prepared_data, exclude_col=['is_canceled'])

# Scale numerical features
scaler, prepared_data = mf.fit_minmax_scaler(prepared_data, scaling_cols)

# Split the data into features and target
X = prepared_data.drop('is_canceled', axis=1)
y = prepared_data['is_canceled']

# Train the model
clf = RandomForestClassifier(
    n_estimators=300,         # Reduced from 300. A good starting point.
    max_depth=17,             # *** THE MOST IMPORTANT CHANGE *** Limits how deep each tree can go.
    min_samples_leaf=1,      # A leaf must have at least 10 samples. Prevents tiny, specific leaves.
    criterion='entropy',      # Kept your choice of criterion.
    bootstrap=True,           # Kept your choice of bootstrap.
    n_jobs=-1,                # Bonus: Use all available CPU cores to speed up training.
    random_state=42           # Bonus: Ensures you get the same result every time you run it.
)
clf.fit(X, y)

# Save the model and encoders
with open("./model/files/rf_model_v3.pkl", "wb") as f:
    pickle.dump(clf, f)
with open("./model/files/catencoder.pkl", "wb") as f:
    pickle.dump(encoder, f)
with open("./model/files/fea_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)