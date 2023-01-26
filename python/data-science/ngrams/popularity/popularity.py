import requests
import json
import matplotlib.pyplot as graph
import numpy
import statistics
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

word = input('Please enter a word to research!\n')
print()

response = requests.get('https://books.google.com/ngrams/json?content=%s&year_start=%s&year_end=%s&corpus=26&smoothing=3' % (word, startYear, endYear))
data = json.loads(response.content)[0]

frame = {}
points = data['timeseries']

frame['word'] = data['ngram']
frame['stdev'] = numpy.std(points)
frame['mean'] = numpy.mean(points)
frame['median'] = numpy.median(points)
frame['mode'] = statistics.mode(points)
frame['range'] = max(points) - min(points)
frame['q1'] = numpy.percentile(points, 25)
frame['q3'] = numpy.percentile(points, 75)
frame['iqr'] = frame['q3'] - frame['q1']

df = pandas.DataFrame([frame])
print(df)

m, b = numpy.polyfit(years, points, 1)

graph.plot(years, points)
graph.plot(years, m * years + b)
graph.title(frame['word'])
graph.ticklabel_format(style='plain')
graph.savefig('%s/%s - %s.png' % (os.path.dirname(os.path.realpath(__file__)), word, yearSpan), dpi=100)
