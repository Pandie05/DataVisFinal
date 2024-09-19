import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the Excel file
file_path = 'data.xlsx'
cleaned_data = pd.read_excel(file_path, sheet_name='Sheet1', header=3)

# Renaming the columns based on their content
cleaned_data.columns = ['model', 'os_version', 'release_date', 'discontinued', 'support_ended', 'final_os', 'lifespan', 'launch_price_max', 'launch_price_min']

# Selecting the relevant columns for analysis
relevant_columns = cleaned_data[['model', 'release_date', 'launch_price_max', 'launch_price_min']]

# Function to extract the maximum price from the 'launch_price_max' column
def extract_max_price(price_str):
    if isinstance(price_str, str):
        price = price_str.split('/')[-1]  # Extract the maximum price
        return float(price.replace('$', '').replace('*', '').replace(',', ''))  # Clean and convert to float
    return np.nan  # Return NaN if price_str is not a string

# Apply the function to extract max prices
relevant_columns['max_price'] = relevant_columns['launch_price_min'].apply(extract_max_price)

# Drop rows with missing model or max_price data
relevant_columns_cleaned = relevant_columns.dropna(subset=['model', 'max_price'])

# Convert the release_date to datetime for future predictions
relevant_columns_cleaned['release_date'] = pd.to_datetime(relevant_columns_cleaned['release_date'], errors='coerce')

# Prepare data for prediction
relevant_columns_cleaned = relevant_columns_cleaned.dropna(subset=['release_date', 'max_price'])
X = (relevant_columns_cleaned['release_date'] - relevant_columns_cleaned['release_date'].min()).dt.days.values.reshape(-1, 1)
y = relevant_columns_cleaned['max_price'].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict iPhone prices for the next 2, 3, 5, and 10 years
future_years = np.array([2, 3, 5, 10]) * 365  # Convert years to days
future_dates = relevant_columns_cleaned['release_date'].max() + pd.to_timedelta(future_years, unit='D')
X_future = (future_dates - relevant_columns_cleaned['release_date'].min()).days.values.reshape(-1, 1)
predicted_prices = model.predict(X_future)

# Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(relevant_columns_cleaned['release_date'].dt.year, relevant_columns_cleaned['max_price'], color='blue', label='Actual Prices')
plt.bar(future_dates.year, predicted_prices, color='red', alpha=0.6, label='Predicted Prices')

# Add labels and title
plt.title('iPhone Prices and Predicted Future Prices')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()