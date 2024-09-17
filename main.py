import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = 'data.xlsx'
excel_data = pd.ExcelFile(file_path)

# Clean the data: Set proper headers and remove irrelevant rows
df_cleaned = pd.read_excel(excel_data, sheet_name='Sheet1', header=2)

# Renaming the columns to more meaningful names
df_cleaned.columns = [
    'Model', 'OS_with', 'Release_date', 'Discontinued', 
    'Support_ended', 'Final_OS', 'Lifespan', 'Lifespan_min', 'Launch_price'
]

# Drop rows where the 'Model' column is NaN (to remove irrelevant data)
df_cleaned.dropna(subset=['Model'], inplace=True)

# Extract years from the 'Lifespan' column
df_cleaned['Lifespan_years'] = df_cleaned['Lifespan'].str.extract(r'(\d+)\s*years').astype(float)

# Set the plot size for better readability
plt.figure(figsize=(10, 6))

# Create a bar chart showing the lifespan of each iPhone model
plt.barh(df_cleaned['Model'], df_cleaned['Lifespan_years'], color='skyblue')

# Add labels and title
plt.xlabel('Lifespan (Years)')
plt.ylabel('iPhone Model')
plt.title('Lifespan of iPhone Models')

# Display the chart
plt.tight_layout()
plt.show()
