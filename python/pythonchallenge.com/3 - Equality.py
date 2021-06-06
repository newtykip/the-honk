import re

data = open('equality.txt'.format(dir)).read()
matches = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', data)
print(matches)