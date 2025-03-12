import pandas as pd
import matplotlib.pyplot as plt

filepath = r'C:\Users\Lindokuhle Yende\OneDrive\Desktop\CodeCollege\python\myCode\chapter16\weather_data\sitka_weather_2021_full.csv'
df = pd.read_csv(filepath)
print(df.head())