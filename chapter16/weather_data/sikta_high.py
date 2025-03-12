# from pathlib import Path
# import csv
# from datetime import datetime
# 
# import matplotlib.pyplot as plt
# 
# 
# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()
# 
# reader = csv.reader(lines)
# header_row = next(reader)
# 
# Extract dates and high temperatures.
# dates, highs = [], []
# for row in reader:
    # current_date = datetime.strptime(row[2], '%Y-%m-%d')
    # high = int(row[4])
    # dates.append(current_date)
    # highs.append(high)

# Plot the high temperatures.
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')
# 
#Format plot.
# ax.set_title("Daily High Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)
# 
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
filepath = r'C:\Users\Lindokuhle Yende\OneDrive\Desktop\CodeCollege\python\myCode\chapter16\weather_data\sitka_weather_2021_simple-original.csv'
df = pd.read_csv(filepath)

print(df.head())

df["DATE"] = pd.to_datetime(df['DATE'])

# Calculate the average temperature for each day
df['TAVG'] = (df['TMAX'] + df['TMIN']) / 2

# Plot the maximum and minimum temperatures
plt.figure(figsize=(12, 6))
plt.plot(df['DATE'], df['TMAX'], label='Maximum Temperature (TMAX)', color='red')
plt.plot(df['DATE'], df['TMIN'], label='Minimum Temperature (TMIN)', color='blue')
plt.plot(df['DATE'], df['TAVG'], label="Average Temperature", color="green", linewidth=5)

# Add labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.title('Daily Maximum and Minimum Temperatures in Sitka, Alaska (2021)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the graph
plt.show()