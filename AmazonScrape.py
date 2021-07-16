import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = 'amazon.com/events/collegedeals'
deals = []

r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')

item = soup.find('', {'' : ''}).findAll('')
cost_min = soup.find('', {'' : ''}).findAll('')
cost_max = soup.find('', {'' : ''}).findAll('')
cost_before = soup.find('', {'' : ''}).findAll('')
pastprice = soup.find('', {'' : ''}).findAll('')

print(r.status_code)
# unfinished