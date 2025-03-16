import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data():
    # Load the dataset
    data = pd.read_csv('screentime_analysis.csv')

    # Check for missing values and duplicates
    if data.isnull().sum().any():
        raise ValueError("Data contains missing values")
    if data.duplicated().sum() > 0:
        raise ValueError("Data contains duplicates")

    # Convert 'Date' column to datetime and extract features
    data['Date'] = pd.to_datetime(data['Date'])
    data['DayOfWeek'] = data['Date'].dt.dayofweek
    data['Month'] = data['Date'].dt.month

    # One-hot encode the 'App' column
    data = pd.get_dummies(data, columns=['App'], drop_first=True)

    # Scale numerical features
    scaler = MinMaxScaler()
    data[['Notifications', 'Times Opened']] = scaler.fit_transform(data[['Notifications', 'Times Opened']])

    # Feature engineering
    data['Previous_Day_Usage'] = data['Usage (minutes)'].shift(1)
    data['Notifications_x_TimesOpened'] = data['Notifications'] * data['Times Opened']

    # Save the preprocessed data
    data.to_csv('preprocessed_screentime_analysis.csv', index=False)
    print("Data preprocessing completed and saved.")

