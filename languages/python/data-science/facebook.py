import requests
import pandas as pd
from bs4 import BeautifulSoup
import pycountry
import json
import os

# Fetch and parse the website
response = requests.get('https://www.statista.com/statistics/268136/top-15-countries-based-on-number-of-facebook-users/')
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Find all of the data points
tds = soup.select('#statTableHTML td')

# Frame the data
data = []

def population(country):
	countryCode = pycountry.countries.search_fuzzy(country)[0].alpha_3
	res = requests.get('https://restcountries.eu/rest/v2/alpha/' + countryCode)
	return int(json.loads(res.content)['population'])

for td1, td2 in zip(tds[::2], tds[1::2]):
	frame = {}
	frame['country'] = td1.text.strip()
	frame['active'] = int(td2.text.strip()) * 1000000
	frame['population'] = population(frame['country'])
	frame['percentActive'] = (frame['active'] / frame['population']) * 100
	data.append(frame)

# Save the data
df = pd.DataFrame(data)
df.to_csv(os.path.dirname(os.path.realpath(__file__)) + '/facebook.csv')
