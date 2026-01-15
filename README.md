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



##  All Qualified Players Ranked by Value

| Rank | Player Name | Season | MPG | PPG | RPG | APG | SPG | BPG | Salary | Value Score |
|------|-------------|--------|-----|-----|-----|-----|-----|-----|--------|-------------|
| 1 | Jose Alvarado | 2022-23 | 21.5 | 9.0 | 2.3 | 3.0 | 1.1 | 0.2 | $1,563,518 | 12.08 |
| 2 | Jose Alvarado | 2024-25 | 24.4 | 10.3 | 2.4 | 4.6 | 1.3 | 0.2 | $1,988,598 | 11.73 |
| 3 | Cole Anthony | 2022-23 | 25.9 | 13.0 | 4.8 | 3.9 | 0.6 | 0.5 | $3,613,680 | 7.45 |
| 4 | Precious Achiuwa | 2022-23 | 20.7 | 9.2 | 6.0 | 0.9 | 0.6 | 0.5 | $2,840,160 | 7.03 |
| 5 | Deni Avdija | 2023-24 | 30.1 | 14.7 | 7.2 | 3.8 | 0.8 | 0.5 | $6,263,188 | 5.05 |
| 6 | Precious Achiuwa | 2023-24 | 24.2 | 7.6 | 7.2 | 1.1 | 0.6 | 1.1 | $4,379,526 | 4.87 |
| 7 | Deni Avdija | 2022-23 | 26.6 | 9.2 | 6.4 | 2.8 | 0.9 | 0.4 | $4,916,160 | 4.78 |
| 8 | Precious Achiuwa | 2023-24 | 21.9 | 7.6 | 6.6 | 1.3 | 0.6 | 0.9 | $4,379,526 | 4.70 |
| 9 | Ochai Agbaji | 2024-25 | 27.2 | 10.4 | 3.8 | 1.5 | 0.9 | 0.5 | $4,310,280 | 4.64 |
| 10 | Cole Anthony | 2023-24 | 22.4 | 11.6 | 3.8 | 2.9 | 0.8 | 0.5 | $5,539,771 | 4.16 |
| 11 | Deni Avdija | 2024-25 | 30.0 | 16.9 | 7.2 | 3.9 | 1.0 | 0.5 | $8,486,619 | 4.06 |
| 12 | Ochai Agbaji | 2022-23 | 20.5 | 7.9 | 2.1 | 1.1 | 0.3 | 0.3 | $3,918,360 | 3.35 |
| 13 | Ochai Agbaji | 2023-24 | 21.1 | 5.8 | 2.8 | 1.1 | 0.6 | 0.6 | $4,114,200 | 3.18 |
| 14 | Kyle Anderson | 2022-23 | 28.4 | 9.4 | 5.3 | 4.9 | 1.1 | 0.9 | $8,780,488 | 3.09 |
| 15 | Grayson Allen | 2023-24 | 33.5 | 13.5 | 3.9 | 3.0 | 0.9 | 0.6 | $8,925,000 | 2.89 |
| 16 | Precious Achiuwa | 2024-25 | 20.5 | 6.6 | 5.6 | 1.0 | 0.8 | 0.7 | $6,275,861 | 2.85 |
| 17 | Nickeil Alexander-Walker | 2023-24 | 23.4 | 8.0 | 2.0 | 2.5 | 0.8 | 0.5 | $7,073,602 | 2.37 |
| 18 | Grayson Allen | 2022-23 | 27.4 | 10.4 | 3.3 | 2.3 | 0.9 | 0.2 | $8,925,000 | 2.23 |
| 19 | Kyle Anderson | 2023-24 | 22.6 | 6.4 | 3.5 | 4.2 | 0.9 | 0.6 | $9,219,512 | 2.15 |
| 20 | Jarrett Allen | 2023-24 | 31.7 | 16.5 | 10.5 | 2.7 | 0.7 | 1.1 | $20,000,000 | 1.84 |
| 21 | OG Anunoby | 2022-23 | 35.6 | 16.8 | 5.0 | 2.0 | 1.9 | 0.7 | $17,357,143 | 1.78 |
| 22 | Steven Adams | 2022-23 | 27.0 | 8.6 | 11.5 | 2.3 | 0.9 | 1.1 | $17,926,829 | 1.66 |
| 23 | Jarrett Allen | 2022-23 | 32.6 | 14.2 | 9.8 | 1.7 | 0.8 | 1.2 | $20,000,000 | 1.63 |
| 24 | OG Anunoby | 2024-25 | 36.6 | 18.0 | 4.8 | 2.2 | 1.5 | 0.9 | $19,928,571 | 1.60 |
| 25 | Jarrett Allen | 2024-25 | 28.0 | 13.5 | 9.7 | 1.9 | 0.9 | 0.9 | $20,000,000 | 1.58 |
| 26 | OG Anunoby | 2023-24 | 34.0 | 14.7 | 4.2 | 2.1 | 1.4 | 0.7 | $18,642,857 | 1.45 |
| 27 | Giannis Antetokounmpo | 2022-23 | 32.1 | 31.1 | 11.8 | 5.7 | 0.8 | 0.8 | $42,492,492 | 1.34 |
| 28 | Bam Adebayo | 2022-23 | 34.6 | 20.4 | 9.2 | 3.2 | 1.2 | 0.8 | $30,351,780 | 1.32 |
| 29 | Giannis Antetokounmpo | 2023-24 | 35.2 | 30.4 | 11.5 | 6.5 | 1.2 | 1.1 | $45,640,084 | 1.28 |
| 30 | Bam Adebayo | 2023-24 | 34.0 | 19.3 | 10.4 | 3.9 | 1.1 | 0.9 | $32,600,060 | 1.28 |
| 31 | Giannis Antetokounmpo | 2024-25 | 34.2 | 30.4 | 11.9 | 6.5 | 0.9 | 1.2 | $48,787,676 | 1.20 |
| 32 | Bam Adebayo | 2024-25 | 34.3 | 18.1 | 9.6 | 4.3 | 1.3 | 0.7 | $34,848,340 | 1.15 |
| 33 | Deandre Ayton | 2022-23 | 30.4 | 18.0 | 10.0 | 1.7 | 0.6 | 0.8 | $30,913,750 | 1.14 |
| 34 | Deandre Ayton | 2023-24 | 32.4 | 16.7 | 11.1 | 1.6 | 1.0 | 0.8 | $32,459,438 | 1.11 |
| 35 | Deandre Ayton | 2024-25 | 30.1 | 14.4 | 10.2 | 1.6 | 0.8 | 1.0 | $34,005,126 | 0.96 |

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
