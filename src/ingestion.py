import pandas as ma


data = ma.read_csv("data/raw/kerala_malayalam_news_supervised.csv", encoding="utf-8")
print(data.head())

print("Dataset Shape:", data.shape)
print("Columns in dataset:", data.columns.tolist())
print("Missing values in dataset:", data.isnull().sum())