import pandas as pd
import matplotlib.pyplot as plt

filepath = r'C:\Users\Lindokuhle Yende\OneDrive\Desktop\CodeCollege\python\myCode\chapter16\weather_data\sitka_weather_2021_full.csv'
df = pd.read_csv(filepath)
print(df.head())

df["DATE"] = pd.to_datetime(df['DATE'])
plt.plot(df['DATE'], df["PRCP"])
plt.xlabel("Date")
plt.ylabel("Precipitaion(Raifall)")
plt.title("Daily rainfall amounts")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()