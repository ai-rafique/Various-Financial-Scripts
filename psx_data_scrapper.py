import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the PSX market summary page
url = "https://www.psx.com.pk/market-summary/"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    if tables:
        all_dataframes = []
        
        for idx, table in enumerate(tables):
            # Extract rows from the table
            rows = table.find_all('tr')
            
            # Extract headers (if available)
            headers = [header.text.strip() for header in rows[0].find_all('th')] if rows[0].find_all('th') else None
            
            # Extract data rows
            data = []
            for row in rows[1:]:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)
            
            # Ensure headers match the number of columns in data
            if headers and len(headers) != len(data[0]):
                headers = [f"Column{i+1}" for i in range(len(data[0]))]
            
            # Create a DataFrame
            df = pd.DataFrame(data, columns=headers if headers else None)
            all_dataframes.append(df)
            
            # Save to CSV
            df.to_csv(f'psx_table_{idx + 1}.csv', index=False)
            print(f"Table {idx + 1} saved as psx_table_{idx + 1}.csv")
    else:
        print("No tables found on the page.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
