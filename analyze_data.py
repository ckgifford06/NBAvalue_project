import pandas as pd

# Load the data
df = pd.read_csv('data/player_stats.csv')

# Filter to just most recent season for each player
df_recent = df.sort_values('SEASON_ID').groupby('PLAYER_NAME').tail(1)

# Calculate points per game (avoid division by zero)
df_recent['PPG'] = df_recent['PTS'] / df_recent['GP'].replace(0, 1)

# Top scorers
print("Top 10 Scorers (PPG):")
print(df_recent.nlargest(10, 'PPG')[['PLAYER_NAME', 'PPG', 'SEASON_ID']])

# Save analyzed data
df_recent.to_csv('data/analyzed_stats.csv', index=False)
print("\nData saved to data/analyzed_stats.csv")