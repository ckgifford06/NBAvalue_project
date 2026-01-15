import pandas as pd

# Load player stats
stats_df = pd.read_csv('data/player_stats.csv')

# Load cleaned salaries
salary_df = pd.read_csv('data/nba_salaries_cleaned.csv')

print(f"Stats data: {len(stats_df)} rows")
print(f"Salary data: {len(salary_df)} rows")

# Merge stats with salaries on player name and season
merged_df = stats_df.merge(
    salary_df[['PLAYER_NAME', 'SEASON_ID', 'Salary']], 
    on=['PLAYER_NAME', 'SEASON_ID'],
    how='inner'
)

print(f"\nMerged data: {len(merged_df)} rows")

# Calculate per-game stats
merged_df['PPG'] = merged_df['PTS'] / merged_df['GP']
merged_df['RPG'] = merged_df['REB'] / merged_df['GP']
merged_df['APG'] = merged_df['AST'] / merged_df['GP']
merged_df['SPG'] = merged_df['STL'] / merged_df['GP']
merged_df['BPG'] = merged_df['BLK'] / merged_df['GP']
merged_df['MPG'] = merged_df['MIN'] / merged_df['GP']

# Create a composite stat score
merged_df['COMPOSITE_SCORE'] = (
    merged_df['PPG'] * 1.0 +      # Points
    merged_df['RPG'] * 1.2 +      # Rebounds
    merged_df['APG'] * 1.5 +      # Assists
    merged_df['SPG'] * 2.0 +      # Steals
    merged_df['BPG'] * 2.0        # Blocks
)

# Calculate value: Composite score per million dollars
merged_df['VALUE_SCORE'] = merged_df['COMPOSITE_SCORE'] / (merged_df['Salary'] / 1_000_000)

# Filter to qualified players (at least 40 games AND 20+ minutes per game)
qualified = merged_df[(merged_df['GP'] >= 40) & (merged_df['MPG'] >= 20)]

print(f"\nQualified players (40+ games, 20+ MPG): {len(qualified)}")

# Sort ALL qualified players by value score (descending)
all_undervalued = qualified.sort_values('VALUE_SCORE', ascending=False)

print("\n" + "="*80)
print("ALL QUALIFIED PLAYERS RANKED BY VALUE (40+ GP, 20+ MPG)")
print("="*80)
print(all_undervalued[[
    'PLAYER_NAME', 'SEASON_ID', 'MPG', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 
    'COMPOSITE_SCORE', 'Salary', 'VALUE_SCORE'
]].to_string(index=False))

# Save results
all_undervalued.to_csv('data/undervalued_players_comprehensive.csv', index=False)
print("\nFull results saved to data/undervalued_players_comprehensive.csv")

# Show some interesting stats
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)
print(f"Total qualified players: {len(qualified)}")
print(f"Average salary: ${qualified['Salary'].mean():,.0f}")
print(f"Average MPG: {qualified['MPG'].mean():.1f}")
print(f"Average composite score: {qualified['COMPOSITE_SCORE'].mean():.2f}")
print(f"Average value score: {qualified['VALUE_SCORE'].mean():.2f}")

# Most efficient player (highest value score)
print("\n" + "="*80)
print("MOST EFFICIENT PLAYER")
print("="*80)
most_efficient = all_undervalued.iloc[0]
print(f"{most_efficient['SEASON_ID']} {most_efficient['PLAYER_NAME']}")
print(f"  MPG: {most_efficient['MPG']:.1f}")
print(f"  PPG: {most_efficient['PPG']:.1f}, RPG: {most_efficient['RPG']:.1f}, APG: {most_efficient['APG']:.1f}")
print(f"  SPG: {most_efficient['SPG']:.1f}, BPG: {most_efficient['BPG']:.1f}")
print(f"  Composite Score: {most_efficient['COMPOSITE_SCORE']:.2f}")
print(f"  Salary: ${most_efficient['Salary']:,.0f}")
print(f"  Value Score: {most_efficient['VALUE_SCORE']:.2f}")

# Least valuable player (lowest value score)
print("\n" + "="*80)
print("LEAST VALUABLE PLAYER")
print("="*80)
least_valuable = all_undervalued.iloc[-1]
print(f"{least_valuable['SEASON_ID']} {least_valuable['PLAYER_NAME']}")
print(f"  MPG: {least_valuable['MPG']:.1f}")
print(f"  PPG: {least_valuable['PPG']:.1f}, RPG: {least_valuable['RPG']:.1f}, APG: {least_valuable['APG']:.1f}")
print(f"  SPG: {least_valuable['SPG']:.1f}, BPG: {least_valuable['BPG']:.1f}")
print(f"  Composite Score: {least_valuable['COMPOSITE_SCORE']:.2f}")
print(f"  Salary: ${least_valuable['Salary']:,.0f}")
print(f"  Value Score: {least_valuable['VALUE_SCORE']:.2f}")