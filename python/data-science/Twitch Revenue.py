import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import os

TIER1PRICE = 4.99
TIER2PRICE = 9.99
TIER3PRICE = 24.99
TIER1EARNING = 2.50
TIER2EARNING = 5
TIER3EARNING = 15

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def getRows(page):
	time.sleep(1)
	response = requests.get('https://twitchtracker.com/subscribers?page=%i' % (page), headers=headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	trs = soup.select('#channels tr')
	if len(trs) > 0:
		del trs[0]
	print('Processed page %i' % (page))
	return trs

howMany = int(input('How many pages would you like to scrape? There are 20 streamers a page.\n'))
data = []

for i in range(howMany):
	trs = getRows(i + 1)
	if len(trs) > 0:
		# Remove dividers from the table
		for count, tr in enumerate(trs, 1):
			if count % 11 == 0:
				i = trs.index(tr)
				del trs[i]
		for row in trs:
			frame = {}
			tds = row.select('td')
			# Filters out rows without full stas
			fullStats = True
			if len(tds) != 11:
				fullStats = False
			for td in tds:
				if td.text.strip().__contains__('?'):
					fullStats = False
			frame['channelName'] = tds[3].text.strip()
			# Fill in the stats if they are full
			if fullStats == True:
				tier1 = int(tds[8].text)
				tier2 = int(tds[9].text)
				tier3 = int(tds[10].text)
				prime = int(tds[6].text)
				totalCost = (tier1 * TIER1PRICE) + (tier2 * TIER2PRICE) + (tier3 * TIER3PRICE)
				totalEarnings = (tier1 * TIER1EARNING) + (tier2 * TIER2EARNING) + (tier3 * TIER3EARNING)
				frame['totalSubs'] = int(tds[4].text)
				frame['totalCostOfSubs'] = totalCost
				frame['twitchCuts'] = totalCost - totalEarnings
				frame['totalEarnings'] = totalEarnings + (prime * TIER1EARNING)
			# Append
			data.append(frame)

df = pd.DataFrame(data, index=None)
df.index += 1
df.to_csv(os.path.dirname(os.path.realpath(__file__)) + '/twitchrevenue.csv')
