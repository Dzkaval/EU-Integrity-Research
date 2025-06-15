import requests
from bs4 import BeautifulSoup
import json

url = "https://data.un.org/Handlers/DataHandler.ashx?" \
      "Service=query&Anchor=tableCode%3a26&Applied=refYear%3a2022&DataMartId=POP&UserQuery" \
      "=&c=2,3,6,8,10,12,14,15,16&s=_countryEnglishNameOrderBy:asc,refYear:" \
      "desc,areaCode:asc&RequestId=424Code:asc&RequestId=773"

url_dict = ["https://data.un.org/Handlers/DataHandler.ashx?Service=query&'
            'DataFilter=tableCode%3a26%3brefYear%3a2021&DataMartId=POP&User'
            'Query=&c=2,3,6,10,12,14,15,16&s=_countryEnglishNameOrderBy:asc'
            ',refYear:desc,areaCode:asc&RequestId=474",
            "https://data.un.org/Handlers/DataHandler.ashx?" \
            "Service=query&Anchor=tableCode%3a26&Applied=refYear%3a2022&DataMartId=POP&UserQuery" \
            "=&c=2,3,6,8,10,12,14,15,16&s=_countryEnglishNameOrderBy:asc,refYear:" \
            "desc,areaCode:asc&RequestId=424Code:asc&RequestId=773"
            ]

def get_etnicity():


# Make the request
response = requests.get(url, verify=False)

# Parse the HTML data with BS4
soup = BeautifulSoup(response.text, "html.parser")

# Find the first table in the data
table = soup.find('table')

# Find all rows in the table
rows = table.find_all('tr')

# Get headers by extracting text from the first row (th -> table headers)
headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

data = []

# For each row (skipping the first row which contains the table header)
for row in rows[1:]:
    # Find all the columns
    cols = row.find_all('td')

    # Get the text from each column
    cols_text = [col.get_text(strip=True) for col in cols]

    # Create a dictionary item for the row
    item = {headers[i]: cols_text[i] for i in range(len(headers))}

    # Add the item to the data array
    data.append(item)

# To convert python list of dictionaries to a JSON string and print it:
json_data = json.dumps(data, indent=4)
print(json_data)