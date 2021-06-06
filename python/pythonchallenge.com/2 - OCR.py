import urllib.request
import re

html = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().decode()
comments = re.findall('<!--(.*?)-->', html, re.DOTALL)
data = comments[-1]

count = {}
for c in data:
    count[c] = count.get(c, 0) + 1

print(count) # equality is rare