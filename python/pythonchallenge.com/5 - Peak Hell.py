import pickle
import urllib.request

raw = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.load(raw)

for line in data:
    print(''.join([k * v for k, v in line]))