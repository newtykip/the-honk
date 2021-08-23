import urllib.request
import json
import os

def getPage(number):
	return json.loads(urllib.request.urlopen('https://gdbrowser.com/api/search/*?diff=1&count=500&type=mostliked&page={0}'.format(number)).read().decode())

def parseLevel(level):
	if level['stars'] == 2:
			print('Adding {0}'.format(level['name']))
			# id, name
			lines.append('{0},{1},{2}\n'.format(level['id'], level['name']))

def saveFile():
	file.flush()
	os.fsync(file.fileno())

number = 0
page = getPage(number)
lines = []

file = open(os.path.dirname(os.path.realpath(__file__)) + '/2stars_res.csv', 'r+')
file.truncate(0)

while page != -1:
	for level in page:
		parseLevel(level)
	number += 1
	print('Page {0} parsed! Moving to page {1}'.format(number - 1, number))
	if len(lines) > 0:
		file.writelines(lines)
		saveFile()
		lines = []
	page = getPage(number)

file.close()
