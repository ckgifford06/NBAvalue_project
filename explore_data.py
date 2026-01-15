import pandas as pd

# Load your data
df = pd.read_csv('data/player_stats.csv')

# See the first few rows
print("First 5 rows:")
print(df.head())

# See what columns you have
print("\nColumn names:")
print(df.columns.tolist())

# Basic stats
print("\nDataset shape (rows, columns):")
print(df.shape)

# See data types
print("\nData types:")
print(df.dtypes)