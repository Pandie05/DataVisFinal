import pandas as pd
import matplotlib.pyplot as plt

appleData_csv = 'csv/SeedUnofficialAppleData.csv'

apple_df = pd.read_csv(appleData_csv)

print(apple_df)