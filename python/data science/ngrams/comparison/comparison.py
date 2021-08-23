import statistics
import requests
import json
import matplotlib.pyplot as plt
import numpy
import os
import pandas

pandas.options.display.float_format = '{:.10f}'.format

words = input('Please enter a list of words. Separate each word with a comma (:\n')
print()
startYear = 1800
endYear = 2019
years = range(startYear, endYear + 1)

response = requests.get('https://books.google.com/ngrams/json?content=%s&year_start=%s&year_end=%s&corpus=26&smoothing=3' % (words, startYear, endYear))
data = json.loads(response.content)

frames = []

for x in data:
	frame = {}
	frame['word'] = x['ngram']
	frame['stdev'] = numpy.std(x['timeseries'])
	frame['mean'] = numpy.mean(x['timeseries'])
	frame['median'] = numpy.median(x['timeseries'])
	frame['mode'] = statistics.mode(x['timeseries'])
	frame['range'] = max(x['timeseries']) - min(x['timeseries'])
	frame['q1'] = numpy.percentile(x['timeseries'], 25)
	frame['q3'] = numpy.percentile(x['timeseries'], 75)
	frame['iqr'] = frame['q3'] - frame['q1']
	frames.append(frame)
	plt.plot(years, x['timeseries'], label=frame['word'])

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
		df.to_csv('%s/%s.csv' % (dirName, wordList))
		break
	if toSave == 'n':
		break

# Save Graph
while True:
	toSave = input('Would you like to save a graph of the data? (y/n)').lower()
	if toSave == 'y':
		plt.ticklabel_format(style='plain')
		plt.legend()
		plt.savefig('%s/%s.png' % (dirName, wordList), dpi=100)
		exit()
	elif toSave == 'n':
		exit()

