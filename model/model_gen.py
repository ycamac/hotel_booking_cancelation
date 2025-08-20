##################################################################################
# The following file is responsible for generating the model, encoder, and scaler
##################################################################################
import pandas as pd
import functions as mf
import pickle

from os import path
from time import time

from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestClassifier
##################################################################################
print("Readind Dataset...")
data = pd.read_csv('./model/files/hotel_bookings.csv')

# Preprocess the data
print("Preprocessing...")
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
print("Spliting the data...")
X = prepared_data.drop('is_canceled', axis=1)
y = prepared_data['is_canceled']

##################################################################################

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, 
    test_size=0.3,    # 30% of the data goes to testing, 70% for training
    random_state=42,  # ensures reproducibility (same split every time)
    stratify=y        # keeps the same proportion of classes in train/test
)

# Set up the model
print("Setting up the classifier...")
clf = RandomForestClassifier(
    n_estimators=100,         # Reduced from 300. A good starting point.
    max_depth=100,             # *** THE MOST IMPORTANT CHANGE *** Limits how deep each tree can go.
    criterion='entropy',      # Kept your choice of criterion.
    min_samples_leaf=2,
    n_jobs=-1,                # Bonus: Use all available CPU cores to speed up training.
    random_state=42           # Bonus: Ensures you get the same result every time you run it.
)

folds = 10
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro','roc_auc']

# Calculate cross-validation scores
# Start timer
start_time = time()
print("Starting Cross Validation with Training Dataset...")
cv_results = cross_validate(clf, X_train, y_train, cv=folds, scoring=scoring, return_train_score=False)
# Stop timer
end_time = time()
elapsed_time = end_time - start_time
print(f"Training time: {elapsed_time:.2f} seconds")

# Put results into a DataFrame for clarity
results_df = pd.DataFrame(cv_results)

# Show per-fold results
# print("Per-fold results:")
# print(results_df)

# Show mean of each metric
print("\nMean metrics:")
print(results_df.mean())

# After CV, train the final model on the entire training set
print('Training the final model...')
model = clf.fit(X_train, y_train)

# Evaluate on the test set
print('Evaluate on Test Dataset')
test_score = model.score(X_test, y_test)
print("Test score:", test_score)

# Show hyperparameters
print("Classifier hyper-paremeters: ")
print(clf.get_params())

##################################################################################

# Save the model and encoders
with open("./model/files/rf_model_v4.pkl", "wb") as f:
    pickle.dump(clf, f)
# with open("./model/files/catencoder.pkl", "wb") as f:
#     pickle.dump(encoder, f)
# with open("./model/files/fea_scaler.pkl", "wb") as f:
#     pickle.dump(scaler, f)


model_size_mb = path.getsize("./model/files/rf_model_v3.pkl") / (1024 * 1024)
print(f"Model size: {model_size_mb:.2f} MB")


# 1. CV metrics mean
cv_mean_metrics = results_df[[f'test_{metric}' for metric in scoring]].mean().to_dict()  # only keep the metrics we scored
# -----------------------------
# 2. Test score
cv_mean_metrics['test_score'] = test_score
# -----------------------------
# 3. Hyperparameters
hyperparams = clf.get_params()
cv_mean_metrics['hyperparams'] = hyperparams
# -----------------------------
# 5. Training time
cv_mean_metrics['training_time'] = elapsed_time
# -----------------------------
# 6. Model size
cv_mean_metrics['model_size_mb'] = model_size_mb
# -----------------------------
# 7. Combine into a single DataFrame

# Convert metrics dict to DataFrame
metrics_df = pd.DataFrame([cv_mean_metrics])

# Optionally, save to CSV
metrics_df.to_csv("./model/files/model_summary.csv", index=False)