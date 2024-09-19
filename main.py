import pandas as pd
import matplotlib.pyplot as plt

# def extract_lifespan(lifespan):

#     years = 0
#     months = 0

#     check_year = re.search(r'(\d+)\s*year')
#     check_month = re.search(r'(\d)\s*month')

#     if check_year
# Returns the model value if the initial value is 'iPhone', otherwise delete 'iPhone' from string
def shorten_Model(model):
    return model if model.strip() == 'iPhone' else model.replace('iPhone', '').strip()

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
print(df_cleaned)
add_6_plus = {
    'Model': 'iPhone 6 Plus', 
    'OS_with': 'iOS 8.0', 
    'Release_date': 'September 19, 2014',
    'Discontinued': 'September 7, 2016',
    'Support_ended': 'November 5, 2020',
    'Final_OS': 'iOS 12.4.9',
    'Lifespan': '4 years, 11 months',
    'Lifespan_min': '3 years',
    'Launch_price': '$299/$399/$499'}

add_6s_plus = {
    'Model': 'iPhone 6S Plus', 
    'OS_with': 'iOS 9.0.1', 
    'Release_date': 'September 25, 2015',
    'Discontinued': 'September 12, 2018',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '5 years, 1 month',
    'Lifespan_min': '2 years, 2 months',
    'Launch_price': '$299/$399/$499'}

add_7_plus = {
    'Model': 'iPhone 7 Plus', 
    'OS_with': 'iOS 10.0.1', 
    'Release_date': 'September 16, 2018',
    'Discontinued': 'September 10, 2019',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '4 years, 2 months',
    'Lifespan_min': '1 year, 2 months',
    'Launch_price': '$319/$419/$519'}

add_8_plus = {
    'Model': 'iPhone 8 Plus', 
    'OS_with': 'iOS 11.0', 
    'Release_date': 'September 22, 2017',
    'Discontinued': 'April 15, 2020',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '3 years',
    'Lifespan_min': '',
    'Launch_price': '$799/$949'}

add_xs_max = {
    'Model': 'iPhone XS Max', 
    'OS_with': 'iOS 12.0', 
    'Release_date': 'September 21, 2018',
    'Discontinued': 'September 10',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '2 years',
    'Lifespan_min': '1 year',
    'Launch_price': '$1099/$1249/$1449'}

add_11_pro_max = {
    'Model': 'iPhone 11 Pro Max', 
    'OS_with': 'iOS 13.0', 
    'Release_date': 'September 20, 2019',
    'Discontinued': 'October 13, 2020',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '1 year, 2 month',
    'Lifespan_min': '',
    'Launch_price': '$1099/$1249/1449'}

add_12_mini = {
    'Model': 'iPhone 12 Mini', 
    'OS_with': 'iOS 14.1', 
    'Release_date': 'October 23, 2020',
    'Discontinued': '',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '0 months',
    'Lifespan_min': '',
    'Launch_price': '$799/$849/$949'}

add_12_pro_max = {
    'Model': 'iPhone 12 Pro Max', 
    'OS_with': 'iOS 14.1', 
    'Release_date': 'October 23, 2020',
    'Discontinued': '',
    'Support_ended': 'current',
    'Final_OS': 'latest iOS',
    'Lifespan': '0 months',
    'Lifespan_min': '',
    'Launch_price': '$1099/$1199/$1399'}

df_cleaned.loc[21] = add_6_plus
df_cleaned.loc[23] = add_6s_plus
df_cleaned.loc[26] = add_7_plus
df_cleaned.loc[30] = add_8_plus
df_cleaned.loc[34] = add_xs_max
df_cleaned.loc[38] = add_11_pro_max
df_cleaned.loc[41] = add_12_mini
df_cleaned.loc[43] = add_12_pro_max
print(df_cleaned)

df_cleaned['Model'] = df_cleaned['Model'].str.split(' /').str[0]

# Drop rows where the 'Model' column is NaN (to remove irrelevant data)
df_cleaned.dropna(subset=['Model'], inplace=True)

# df_cleaned['Model'] = df_cleaned['Model'].str.replace('iPhone', '').str.strip()
# Applies shorten_Model function to each item in the Model column
df_cleaned['Model'] = df_cleaned['Model'].apply(shorten_Model)
print(df_cleaned)

# Extract years from the 'Lifespan' column
df_cleaned['Lifespan_years'] = df_cleaned['Lifespan'].str.extract(r'(\d+)\s*year').astype(float)

print(df_cleaned)

df_cleaned['Price'] = df_cleaned['Launch_price'].str.extract(r'\$(\d+)').astype(float)
print(df_cleaned['Price'])
# Set the plot size for better readability
plt.figure(figsize=(8, 6))

# Create a bar chart showing the lifespan of each iPhone model
# plt.bar(df_cleaned['Model'], df_cleaned['Lifespan_years'], color='skyblue')

# Add labels and title
# plt.xlabel('Lifespan (Years)')
# plt.ylabel('iPhone Model')
# plt.title('Lifespan of iPhone Models')

# plt.bar(df_cleaned['Lifespan_years'], df_cleaned['Price'], color='green')

# plt.xlabel('Launch Price (USD)')
# plt.ylabel('iPhone Model')
# plt.title('Lifespan of iPhone Models')

fig, (bar1, bar2) = plt.subplots(1, 2, figsize=(14, 6))

bar1.bar(df_cleaned['Model'], df_cleaned['Lifespan_years'], color='skyblue')
bar1.set_xlabel('iPhone Model')
bar1.set_ylabel('Lifespan (Years)')
bar1.set_title('Lifespan of iPhone Models')
bar1.set_xticklabels(df_cleaned['Model'], rotation=90)

bar2.bar(df_cleaned['Model'], df_cleaned['Price'], color='green')
bar2.set_xlabel('iPhone Model')
bar2.set_ylabel('Launch Price (USD)')
bar2.set_title('iPhone Model Launch Prices')
bar2.set_xticklabels(df_cleaned['Model'], rotation=90)


# Display the chart
plt.tight_layout()
plt.show()