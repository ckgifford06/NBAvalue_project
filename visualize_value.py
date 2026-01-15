import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# Load the data
df = pd.read_csv('data/undervalued_players_comprehensive.csv')

print(f"Creating detailed scatter plot for {len(df)} players...")

# Create the scatter plot
plt.figure(figsize=(16, 12))
scatter = plt.scatter(df['Salary'] / 1_000_000, df['COMPOSITE_SCORE'], 
                     c=df['VALUE_SCORE'], cmap='RdYlGn', 
                     s=150, alpha=0.7, edgecolors='black', linewidth=0.8)

# Add colorbar
cbar = plt.colorbar(scatter, label='Value Score')
cbar.ax.tick_params(labelsize=10)

# Add player names next to each dot
for idx, row in df.iterrows():
    plt.annotate(f"{row['SEASON_ID']} {row['PLAYER_NAME']}", 
                xy=(row['Salary']/1_000_000, row['COMPOSITE_SCORE']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=8, alpha=0.8)

plt.xlabel('Salary (Millions $)', fontsize=14, fontweight='bold')
plt.ylabel('Composite Score (Performance)', fontsize=14, fontweight='bold')
plt.title('NBA Player Value Analysis: Salary vs Performance (2022-2024)\nGreen = Undervalued, Red = Overvalued', 
          fontsize=16, fontweight='bold', pad=20)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('player_value_detailed.png', dpi=300, bbox_inches='tight')
print("✓ Saved: player_value_detailed.png")
plt.close()

print("\nVisualization created successfully!")