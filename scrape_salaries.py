import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://hoopshype.com/salaries/players/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables
    all_tables = soup.find_all('table')
    print(f"\nFound {len(all_tables)} tables")
    
    for i, table in enumerate(all_tables):
        print(f"\nTable {i}:")
        print(f"  Class: {table.get('class')}")
        print(f"  ID: {table.get('id')}")
        
        # Try to extract from first table
        if i == 0:
            rows = []
            tbody = table.find('tbody')
            if tbody:
                for tr in tbody.find_all('tr')[:5]:  # Just first 5 rows
                    cols = [td.text.strip() for td in tr.find_all('td')]
                    if cols:
                        rows.append(cols)
                        print(f"  Sample row: {cols}")
            else:
                print("  No tbody found")