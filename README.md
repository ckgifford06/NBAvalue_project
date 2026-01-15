# NBA Player Value Analysis: Finding the Most Undervalued Players

A data analytics project that identifies undervalued NBA players by analyzing their performance metrics relative to their salaries (2022-2024 seasons).

## Project Overview

This project uses the NBA API and salary data to calculate a comprehensive "value score" for NBA players, revealing which players provide the best performance per dollar spent. The analysis considers multiple statistics including points, rebounds, assists, steals, and blocks.



## 📈 Visualization

![Player Value Analysis](player_value_detailed.png)

*Green dots indicate undervalued players (high performance relative to salary), while red dots indicate overvalued players (low performance relative to salary).*

## Methodology

### Data Sources
- **Player Statistics**: NBA API (`nba_api` Python package)
- **Salary Data**: NBA player salaries (2022-2024)


# Sample Results

Stats data: 157 rows
Salary data: 1214 rows

Merged data: 47 rows

Qualified players (40+ games, 20+ MPG): 35

ALL QUALIFIED PLAYERS RANKED BY VALUE (40+ GP, 20+ MPG)


📊 Top 10 Most Undervalued Players

| Rank | Player Name | Season | MPG | PPG | RPG | APG | SPG | BPG | Salary | Value Score |
|------|-------------|--------|-----|-----|-----|-----|-----|-----|--------|-------------|
| 1 | Jose Alvarado | 2022-23 | 21.5 | 9.0 | 2.3 | 3.0 | 1.1 | 0.2 | $1,563,518 | 12.08 |
| 2 | Jose Alvarado | 2024-25 | 24.4 | 10.3 | 2.4 | 4.6 | 1.3 | 0.3 | $1,988,598 | 11.73 |
| 3 | Cole Anthony | 2022-23 | 25.9 | 13.0 | 4.8 | 3.9 | 0.6 | 0.5 | $3,613,680 | 7.45 |
| 4 | Precious Achiuwa | 2022-23 | 20.7 | 9.2 | 6.0 | 0.9 | 0.6 | 0.5 | $2,840,160 | 7.03 |
| 5 | Deni Avdija | 2023-24 | 30.1 | 14.7 | 7.2 | 3.8 | 0.8 | 0.5 | $6,263,188 | 5.05 |

Full results saved to data/undervalued_players_comprehensive.csv


SUMMARY STATISTICS

Total qualified players: 35
Average salary: $16,327,634
Average MPG: 28.4
Average composite score: 29.64
Average value score: 3.29


MOST EFFICIENT PLAYER

2022-23 Jose Alvarado
  MPG: 21.5
  PPG: 9.0, RPG: 2.3, APG: 3.0
  SPG: 1.1, BPG: 0.2
  Composite Score: 18.89
  Salary: $1,563,518
  Value Score: 12.08


LEAST VALUABLE PLAYER

2024-25 Deandre Ayton
  MPG: 30.1
  PPG: 14.4, RPG: 10.2, APG: 1.6
  SPG: 0.8, BPG: 1.0
  Composite Score: 32.48
  Salary: $34,005,126
  Value Score: 0.96


## 📝 Insights

- Players on rookie contracts tend to provide exceptional value
- Guard positions often show higher value scores due to assists and steals
- Role players with strong defensive stats (steals/blocks) are frequently undervalued

This project is open source and available under the [MIT License](LICENSE).
