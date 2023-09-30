import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

# Headers for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL of the page to be scraped
url = 'https://www.wsj.com/market-data/quotes/AAPL/financials/annual/income-statement'

# Send a GET request to the server
page = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')  # Parse the page content

    # Try to find the table with the specified class name
    tables = soup.find_all('table', {'class': 'cr_dataTable'})

    # Check if any tables were found
    if tables:
        print("Table found!")  # Print a message if a table is found

        # Process the found table(s)
        for table in tables:
            html_content = str(table)  # Convert the table to a string
            html_io = StringIO(html_content)  # Create a StringIO object from the string
            df = pd.read_html(html_io)[0]  # Read the HTML content as a DataFrame

            print(df.head())  # Print the first 5 rows of the DataFrame

    else:
        print("No tables found with the specified class name.")  # Print a message if no table is found

else:
    print(f"Failed to retrieve content. Status code: {page.status_code}")  # Print an error message if the request is not successful
