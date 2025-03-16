import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def train_model():
    # Load the preprocessed data
    data = pd.read_csv('preprocessed_screentime_analysis.csv')

    # Split data into features and target variable
    X = data.drop(columns=['Usage (minutes)', 'Date'])
    y = data['Usage (minutes)']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f'Mean Absolute Error: {mae}')

    # Save the trained model
    import joblib
    joblib.dump(model, 'random_forest_model.pkl')
    print("Model training completed and saved.")

