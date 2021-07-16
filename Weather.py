import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = f'https://weather.com/weather/today/l/77a3de8c57dc87ed3e335e97d6bfbed46d846db5a7db63c55ea0dff237bcf4ff'

r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')

city = soup.find('div', {'class' : 'CurrentConditions--header--1NDhO'}).find('h1').text
time = soup.find('div', {'class' : 'CurrentConditions--header--1NDhO'}).find('div').text
temp = soup.find('div', {'class' : 'CurrentConditions--primary--39Y3f'}).findAll()[0].text
hum = soup.find('div', {'class' : 'CurrentConditions--primary--39Y3f'}).findAll()[1].text
chance = soup.find('div', {'data-testid' : 'precipPhrase'}).find('span').text

# forecast:
morning = soup.find('div', {'data-testid' : 'SegmentHighTemp'}).find().text
afternoon = soup.find('div', {'class' : ''})
evening = soup.find('div', {'class' : ''})
overnight = soup.find('div', {'class' : ''})

print('Location: ' + city[:-7])
print('The temperature is ' + temp + ' with ' + hum + ', ' + time)