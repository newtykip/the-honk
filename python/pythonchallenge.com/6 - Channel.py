import zipfile
import re

f = zipfile.ZipFile('channel.zip')
num = '90052'
comments = []

while True:
    content = f.read('{0}.txt'.format(num)).decode('utf-8')
    comments.append(f.getinfo('{0}.txt'.format(num)).comment.decode('utf-8'))
    print(content)
    match = re.search('Next nothing is (\d+)', content)
    if match == None:
        break
    num = match.group(1)

print(''.join(comments))