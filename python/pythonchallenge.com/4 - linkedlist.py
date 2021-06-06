import urllib.request
import re

uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
num = str(16044 / 2)
pattern = re.compile('and the next nothing is (\d+)')

while True:
    content = urllib.request.urlopen(uri % num).read().decode()
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)