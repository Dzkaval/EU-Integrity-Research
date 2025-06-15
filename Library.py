import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

eu_website = ['https://european-union.europa.eu/principles-countries-history/eu-countries_en?page=0',
              'https://european-union.europa.eu/principles-countries-history/eu-countries_en?page=1']

EU_countries = []

for url in eu_website:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    countries = soap.select('a.ecl-link ecl-link--standalone')
    for country in countries:
        EU_countries.append(country.text.strip())

all_countries_req = ('https://restcountries.com/v3.1/region/europe?fields=name,region,subregion,cca2,'
                     'population,unMember')

response = requests.get(all_countries_req, verify=True)

data = response.json()

rows = []

for country in data:
    if country['unMember'] == True:
        name = country['name']['common']
        region = country['region']
        subregion = country['subregion']
        code = country['cca2']
        population = country.get('population', None)

        rows.append([code, name, region, subregion, population])

    focused_countries = pd.DataFrame(rows, columns=['code', 'name', 'region','subregion', 'population'])

print(focused_countries)

focused_countries.to_excel('countries.xlsx', sheet_name='general df', index=False)



