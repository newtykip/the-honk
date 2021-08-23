import requests
from bs4 import BeautifulSoup
import pandas
import os

# Fetch and parse the website
response = requests.get('https://realpython.github.io/fake-jobs/')
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Find all of the jobs
jobList = soup.find(id='ResultsContainer')
jobs = jobList.find_all('div', class_='card-content')

# Frame the data
data = []

def formatElement(el):
    return el.text.strip()

for job in jobs:
    frame = {}
    frame['title'] = formatElement(job.find('h2', class_='title'))
    frame['company'] = formatElement(job.find('h3', class_='company'))
    frame['location'] = formatElement(job.find('p', class_='location'))
    data.append(frame)

# Save the data
df = pandas.DataFrame(data)
df.to_csv(os.path.dirname(os.path.realpath(__file__)) + '/fakejobs_res.csv')
