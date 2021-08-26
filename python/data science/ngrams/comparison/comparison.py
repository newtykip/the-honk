import statistics
import requests
import json
import matplotlib.pyplot as plt
import numpy
import os
import pandas

def yearInput(text):
	while True:
		try:
			x = int(input(text + '\n'))
		except ValueError:
			print('You must input an integer!\n')
		else:
			if x > 2019 or x < 1500:
				print('The year inputted is out of range. It must be between 1500 and 2019!')
			else:
				return x

pandas.options.display.float_format = '{:.10f}'.format

startYear = yearInput('Please enter the start year!')
endYear = yearInput('Please enter the end year!')
yearSpan = '%i-%i' % (startYear, endYear)
years = range(startYear, endYear + 1)

words = input('Please enter a list of words. Separate each word with a comma (:\n')
print()

response = requests.get('https://books.google.com/ngrams/json?content=%s&year_start=%s&year_end=%s&corpus=26&smoothing=3' % (words, startYear, endYear))
data = json.loads(response.content)

frames = []

for x in data:
	frame = {}
	points = x['timeseries']
	frame['word'] = x['ngram']
	frame['stdev'] = numpy.std(points)
	frame['mean'] = numpy.mean(points)
	frame['median'] = numpy.median(points)
	frame['mode'] = statistics.mode(points)
	frame['range'] = max(points) - min(points)
	frame['q1'] = numpy.percentile(points, 25)
	frame['q3'] = numpy.percentile(points, 75)
	frame['iqr'] = frame['q3'] - frame['q1']
	frames.append(frame)
	plt.plot(years, points, label=frame['word'])

df = pandas.DataFrame(frames)
print(df)

# Summary Statistics
for frame in frames:
	print()
	if frame['stdev'] == max([ f['stdev'] for f in frames ]):
		print('%s has the highest standard deviation!' % (frame['word']))
	elif frame['stdev'] == min([ f['stdev'] for f in frames ]):
		print('%s has the lowest standard deviation!' % (frame['word']))

# Save CSV
dirName = os.path.dirname(os.path.realpath(__file__))
wordList = ', '.join([f['word'] for f in frames])

while True:
	toSave = input('Would you like to save this data frame in a CSV? (y/n)')
	if toSave == 'y':
		df.to_csv('%s/%s - %s.csv' % (dirName, wordList, yearSpan))
		break
	if toSave == 'n':
		break

# Save Graph
while True:
	toSave = input('Would you like to save a graph of the data? (y/n)').lower()
	if toSave == 'y':
		plt.ticklabel_format(style='plain')
		plt.legend()
		plt.savefig('%s/%s - %s.png' % (dirName, wordList, yearSpan), dpi=100)
		exit()
	elif toSave == 'n':
		exit()

