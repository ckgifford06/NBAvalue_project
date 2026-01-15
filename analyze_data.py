import pandas as pd

df = pd.read_csv('data/player_stats.csv')

df_recent = df.sort_values('SEASON_ID').groupby('PLAYER_NAME').tail(1)

df_recent['PPG'] = df_recent['PTS'] / df_recent['GP'].replace(0, 1)

print("Top 10 Scorers (PPG):")
print(df_recent.nlargest(10, 'PPG')[['PLAYER_NAME', 'PPG', 'SEASON_ID']])

df_recent.to_csv('data/analyzed_stats.csv', index=False)
print("\nData saved to data/analyzed_stats.csv")
