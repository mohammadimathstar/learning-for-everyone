import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error

def monitor_model():
    # Load the preprocessed data
    data = pd.read_csv('preprocessed_screentime_analysis.csv')

    # Load the deployed model
    model = joblib.load('deployed_model.pkl')

    # Split data into features and target variable
    X = data.drop(columns=['Usage (minutes)', 'Date'])
    y = data['Usage (minutes)']

    # Make predictions
    predictions = model.predict(X)

    # Evaluate the model
    mae = mean_absolute_error(y, predictions)
    print(f'Mean Absolute Error: {mae}')

    # Define the accuracy threshold
    accuracy_threshold = 10.0  # Example threshold

    # Check if the model's performance is below the threshold
    if mae > accuracy_threshold:
        print("Model performance is below the threshold. Triggering retraining...")
        # Trigger retraining process (e.g., by calling the train_model function)
        train_model()
    else:
        print("Model performance is satisfactory.")

