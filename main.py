import requests

endpoint = 'https://query.wikidata.org/sparql'

sparql_query = """SELECT ?country ?countryLabel WHERE {
  ?country wdt:P463 wd:Q458.  # P463: "member of", Q458: "European Union"

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY ?countryLabel"""

params = {
    "query": sparql_query,
    "format": "json"  # Specify the response format (JSON in this case)
}

response = requests.get(endpoint, params=params)

if response.status_code == 200:
    # Parse and print the JSON response
    data = response.json()
    for result in data["results"]["bindings"]:
        country = result["country"]["value"]
        country_label = result["countryLabel"]["value"]
        print(f"Label: {country_label}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the raw response for debugging