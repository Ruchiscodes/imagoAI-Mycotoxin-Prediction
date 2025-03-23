import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load the trained model
MODEL_PATH = "cnn_model.h5"
model = load_model(MODEL_PATH)

# Get expected input shape
expected_features = model.input_shape[1]

# Streamlit UI
st.title("Hyperspectral Imaging Mycotoxin Predictor")
st.write("Upload spectral data to predict mycotoxin levels in corn samples.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview:")
    st.dataframe(data.head())

    try:
        # Drop non-numeric columns
        numeric_data = data.select_dtypes(include=[np.number])
        
        # Ensure correct number of features
        num_features = numeric_data.shape[1]
        if num_features == 0:
            st.error("No numeric features found. Please check your input file.")
            st.stop()
        
        if num_features > expected_features:
            numeric_data = numeric_data.iloc[:, :expected_features]  # Trim extra columns
        elif num_features < expected_features:
            st.error(f"Uploaded data has {num_features} features, but the model expects {expected_features}. Please check your input file.")
            st.stop()
        
        # Convert to numpy array
        X = numeric_data.values.astype(np.float32)
        
        # Standardization (adjust based on your preprocessing pipeline)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Reshape for CNN (adjust dimensions if necessary)
        X_reshaped = X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1))
        
        # Make predictions
        predictions = model.predict(X_reshaped)
        
        # Display results
        st.write("### Predictions:")
        st.dataframe(pd.DataFrame(predictions, columns=["Predicted Mycotoxin Level"]))
    
    except Exception as e:
        st.error(f"Error processing data: {e}")
