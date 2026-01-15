import pandas as pd


df = pd.read_csv('data/player_stats.csv')


print("First 5 rows:")
print(df.head())


print("\nColumn names:")
print(df.columns.tolist())


print("\nDataset shape (rows, columns):")
print(df.shape)


print("\nData types:")
print(df.dtypes)
