# NBA Player Value Analysis: Finding the Most Undervalued Players

A data analytics project that identifies undervalued NBA players by analyzing their performance metrics relative to their salaries (2022-2024 seasons).

## 📊 Project Overview

This project uses the NBA API and salary data to calculate a comprehensive "value score" for NBA players, revealing which players provide the best performance per dollar spent. The analysis considers multiple statistics including points, rebounds, assists, steals, and blocks.

## 🎯 Key Findings

### Most Undervalued Player
**[Season] [Player Name]**
- Salary: $X,XXX,XXX
- Value Score: X.XX
- Stats: XX.X PPG, X.X RPG, X.X APG

### Least Valuable Player
**[Season] [Player Name]**
- Salary: $X,XXX,XXX
- Value Score: X.XX
- Stats: XX.X PPG, X.X RPG, X.X APG

## 📈 Visualization

![Player Value Analysis](player_value_detailed.png)

*Green dots indicate undervalued players (high performance relative to salary), while red dots indicate overvalued players (low performance relative to salary).*

## 🔧 Methodology

### Data Sources
- **Player Statistics**: NBA API (`nba_api` Python package)
- **Salary Data**: NBA player salaries (2022-2024)

### Value Calculation
The composite performance score is calculated as:
```
Composite Score = (PPG × 1.0) + (RPG × 1.2) + (APG × 1.5) + (SPG × 2.0) + (BPG × 2.0)
```

Value Score = Composite Score / (Salary in millions)

### Qualification Criteria
- Minimum 40 games played
- Minimum 20 minutes per game

## 💻 Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **matplotlib & seaborn** - Data visualization
- **nba_api** - Fetching NBA statistics
- **BeautifulSoup & requests** - Web scraping (attempted)

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nba-value-analysis.git
cd nba-value-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the analysis:
```bash
# Fetch NBA stats
python fetch_data.py

# Clean salary data
python clean_salaries.py

# Analyze and find undervalued players
python find_undervalued.py

# Generate visualizations
python visualize_value.py
```

## 📁 Project Structure
```
nba-value-analysis/
├── data/
│   ├── player_stats.csv
│   ├── nba_salaries_cleaned.csv
│   └── undervalued_players_comprehensive.csv
├── fetch_data.py
├── clean_salaries.py
├── analyze_data.py
├── find_undervalued.py
├── visualize_value.py
├── player_value_detailed.png
├── requirements.txt
└── README.md
```

## 📊 Sample Results

| Rank | Player Name | Season | Salary | Value Score |
|------|-------------|--------|--------|-------------|
| 1 | [Player] | 2023-24 | $X.XM | X.XX |
| 2 | [Player] | 2022-23 | $X.XM | X.XX |
| 3 | [Player] | 2024-25 | $X.XM | X.XX |

## 🔮 Future Improvements

- [ ] Expand analysis to include historical data (1990-2022)
- [ ] Adjust salaries for inflation using CPI data
- [ ] Add advanced metrics (PER, Win Shares, VORP)
- [ ] Build interactive Streamlit dashboard
- [ ] Include playoff performance data
- [ ] Analyze value by position and team

## 📝 Insights

- Players on rookie contracts tend to provide exceptional value
- Guard positions often show higher value scores due to assists and steals
- Role players with strong defensive stats (steals/blocks) are frequently undervalued

## 👤 Author

[Your Name]
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
