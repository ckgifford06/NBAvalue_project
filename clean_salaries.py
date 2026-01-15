import pandas as pd
import re

salary_df = pd.read_csv('data/playerSalaries.csv')

print("Original salary data:")
print(salary_df.head())

def clean_salary(salary_str):
    if pd.isna(salary_str) or salary_str == '$0' or salary_str == 0:
        return 0
    # Remove $, commas, and spaces
    cleaned = re.sub(r'[\$,\s]', '', str(salary_str))
    try:
        return float(cleaned)
    except:
        return 0

salary_columns = ['2022/2023', '2023/2024', '2024/2025']

for col in salary_columns:
    if col in salary_df.columns:
        salary_df[col] = salary_df[col].apply(clean_salary)

salary_long = pd.melt(
    salary_df, 
    id_vars=['Player Id', 'Player Name'],
    value_vars=salary_columns,
    var_name='Season',
    value_name='Salary'
)

salary_long['SEASON_ID'] = salary_long['Season'].apply(
    lambda x: x.split('/')[0] + '-' + x.split('/')[1][-2:]
)

salary_long = salary_long[salary_long['Salary'] > 0]
salary_long = salary_long.rename(columns={'Player Name': 'PLAYER_NAME'})

print("\nCleaned salary data:")
print(salary_long.head(10))
print(f"\nTotal rows: {len(salary_long)}")

salary_long.to_csv('data/nba_salaries_cleaned.csv', index=False)
print("\nSaved to data/nba_salaries_cleaned.csv")
