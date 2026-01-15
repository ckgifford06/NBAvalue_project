from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
import time
import os

if not os.path.exists('data'):
    os.makedirs('data')

all_players = players.get_active_players()
print(f"Found {len(all_players)} active players")

all_stats = []

for i, player in enumerate(all_players[:20]):
    print(f"Fetching data for {player['full_name']} ({i+1}/{20})")
    
    try:
        career = playercareerstats.PlayerCareerStats(player_id=player['id'])
        stats_df = career.get_data_frames()[0]
        
        stats_df['PLAYER_NAME'] = player['full_name']
        all_stats.append(stats_df)
        
        # Be nice to the API - wait between requests
        time.sleep(0.6)
    except Exception as e:
        print(f"Error fetching {player['full_name']}: {e}")
        continue


combined_df = pd.concat(all_stats, ignore_index=True)

combined_df.to_csv('data/player_stats.csv', index=False)
print("Data saved to data/player_stats.csv")