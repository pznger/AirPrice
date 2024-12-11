import pandas as pd

original_data = pd.read_excel("original_data.xlsx")

weather_data = pd.read_excel("merged_weather_data.xlsx")

merged_data = pd.merge(original_data, weather_data, left_on='Date_of_Journey', right_on='日期', how='left')

merged_data.drop(columns=['日期'], inplace=True)

merged_data.to_csv("merged_data.csv", index=False)
