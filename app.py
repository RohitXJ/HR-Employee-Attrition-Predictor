from flask import Flask, render_template, request, jsonify
import sys
import os
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the prediction function
try:
    from src.predictor import predict_attrition
except ImportError:
    print("Error: Could not import predict_attrition from src/prediction_model.py")
    sys.exit(1)

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles attrition prediction requests.
    Receives JSON data from the frontend, converts it to a pandas DataFrame,
    passes it to the prediction model, and returns the prediction result.
    """
    try:
        data = request.get_json(force=True)
        print("Received raw data for prediction:", data)

        # Convert JSON data to pandas DataFrame.
        # Ensure DataFrame columns match features expected by predict_attrition.
        input_df = pd.DataFrame([data])
        print("Converted to DataFrame for prediction:", input_df)

        # Call the prediction function. It expects a DataFrame and returns '0' or '1'.
        prediction_str = predict_attrition(input_df)

        # Determine the attrition status string
        attrition_status_str = 'Yes' if prediction_str == '1' else 'No'

        # Craft a detailed message based on the prediction
        if attrition_status_str == 'Yes':
            prediction_message = "Based on the provided data, the employee is predicted to LEAVE the company."
        else:
            prediction_message = "Based on the provided data, the employee is predicted to STAY with the company."

        # Return a JSON response to the frontend
        return jsonify({
            'status': 'success',
            'attrition_status': attrition_status_str,
            'prediction_message': prediction_message
        })

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'status': 'error', 'message': f'An internal server error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
