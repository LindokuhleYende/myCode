import pandas as pd 
import matplotlib.pyplot as plt

filepath1 = r'C:\Users\Lindokuhle Yende\OneDrive\Desktop\CodeCollege\python\myCode\chapter16\weather_data\sitka_weather_2021_simple-original.csv'
filepath2 = r'C:\Users\Lindokuhle Yende\OneDrive\Desktop\CodeCollege\python\myCode\chapter16\weather_data\death_valley_2021_full.csv'

df1 = pd.read_csv(filepath1)
df2 = pd.read_csv(filepath2)

print(df1.head())
print(df2.head())

df1["DATE"] = pd.to_datetime(df1['DATE'])
df2["DATE"] = pd.to_datetime(df2['DATE'])

# Calculate the average temperature for each day for sikta
df1['TAVG'] = (df1['TMAX'] + df1['TMIN']) / 2

average = (df2["TMAX"] + df2["TMIN"])/2

plt.plot(df1['DATE'], df1['TAVG'], label="Average Temperature for Sikta", color="green")
plt.plot(df1["DATE"], average, label= "Average Temperature for Death Valley", color= "red")

# Add labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperatures in Sitka Vs Death Valleyc (2021)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the graph
plt.show()