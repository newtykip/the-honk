import requests
import json
import matplotlib.pyplot as graph
import numpy
import statistics
import os
import pandas

pandas.options.display.float_format = '{:.10f}'.format

word = input('Please enter a word to research!\n')
print()
startYear = 1800
endYear = 2019
years = range(startYear, endYear + 1)

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
graph.savefig('%s/%s.png' % (os.path.dirname(os.path.realpath(__file__)), word), dpi=100)
