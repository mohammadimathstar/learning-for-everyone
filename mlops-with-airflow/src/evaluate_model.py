import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error

def evaluate_model():
    # Load the preprocessed data
    data = pd.read_csv('preprocessed_screentime_analysis.csv')

    # Load the trained model
    model = joblib.load('random_forest_model.pkl')

    # Split data into features and target variable
    X = data.drop(columns=['Usage (minutes)', 'Date'])
    y = data['Usage (minutes)']

    # Make predictions
    predictions = model.predict(X)

    # Evaluate the model
    mae = mean_absolute_error(y, predictions)
    print(f'Mean Absolute Error: {mae}')

