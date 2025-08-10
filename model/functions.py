import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

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