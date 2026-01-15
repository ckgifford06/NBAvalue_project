import pandas as pd

# Load data
df = pd.read_csv('data/undervalued_players_comprehensive.csv')

print("## 📊 All Qualified Players Ranked by Value\n")
print("| Rank | Player Name | Season | MPG | PPG | RPG | APG | SPG | BPG | Salary | Value Score |")
print("|------|-------------|--------|-----|-----|-----|-----|-----|-----|--------|-------------|")

for i, (idx, row) in enumerate(df.iterrows(), 1):
    print(f"| {i} | {row['PLAYER_NAME']} | {row['SEASON_ID']} | "
          f"{row['MPG']:.1f} | {row['PPG']:.1f} | {row['RPG']:.1f} | {row['APG']:.1f} | "
          f"{row['SPG']:.1f} | {row['BPG']:.1f} | ${row['Salary']:,.0f} | {row['VALUE_SCORE']:.2f} |")
