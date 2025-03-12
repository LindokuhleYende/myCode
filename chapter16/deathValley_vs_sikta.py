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