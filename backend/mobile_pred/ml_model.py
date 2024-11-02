import os
import sys
import joblib
import pandas as pd

# Set up path configuration
# Add parent directory to Python path to allow imports from other project directories
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Define paths for the trained model and scaler files
model_path = os.path.join(parent_dir, 'ai_models', 'best_model.pkl')
scaler_path = os.path.join(parent_dir, 'ai_models', 'standard_scaler.pkl')

# Validate that required model files exist before proceeding
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")
if not os.path.exists(scaler_path):
    raise FileNotFoundError(f"Scaler file not found at: {scaler_path}")

# Load the pre-trained model and scaling transformer
loaded_model = joblib.load(model_path)
sc = joblib.load(scaler_path)

def preprocess_json_input(json_input, scaler):
    """
    Prepare input data for model prediction
    Args:
        json_input: Dictionary containing feature values
        scaler: StandardScaler object for feature normalization
    Returns:
        Scaled input features ready for model prediction
    """
    # Convert JSON input to DataFrame
    input_df = pd.DataFrame([json_input])
    # Remove ID column if present as it's not used for prediction
    if 'id' in input_df.columns:
        input_df = input_df.drop('id', axis=1)
    # Scale features using the pre-trained scaler
    input_scaled = scaler.transform(input_df)
    return input_scaled

def predict_from_json(json_input, model, scaler):
    """
    Make predictions using the trained model
    Args:
        json_input: Dictionary containing feature values
        model: Trained machine learning model
        scaler: StandardScaler object for feature normalization
    Returns:
        tuple: (predicted_class, confidence_score)
    """
    # Preprocess the input data
    input_scaled = preprocess_json_input(json_input, scaler)
    # Get model predictions
    predictions = model.predict(input_scaled)
    # Get prediction probabilities
    probabilities = model.predict_proba(input_scaled)
    # Calculate confidence score (highest probability)
    confidence = max(probabilities[0])
    return predictions[0], confidence

def predict_price(parameter):
    """
    Main prediction function that returns the predicted price range
    Args:
        parameter: Dictionary containing mobile phone features
    Returns:
        int: Predicted price range category
    """
    predicted_class, confidence = predict_from_json(parameter, loaded_model, sc)
    return int(predicted_class)



