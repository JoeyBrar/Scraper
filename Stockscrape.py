import requests
from bs4 import BeautifulSoup

amount = None
myStocks = []
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

while True:
    try:
        amount = int(input('How many stocks do you have? (Enter as a number): '))
        if type(amount) == int:
            break
    except ValueError:
        print('I told you to enter a number!')
    except TypeError:
        print('I told you to enter a number!')
        

for count in range(amount):
    add = str(input('What are your stock symbols? (Enter one by one, seperatly): '))
    myStocks.append(add)

print('\n')

for count in range(len(myStocks)):
    Symbol = myStocks[count]
    url = f'https://finance.yahoo.com/quote/{Symbol}'

    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')

    try:
        # findAll always returns in a list form, so we can index it.
        price = soup.find('div', class_ = 'D(ib) Mend(20px)').findAll('span')[0].text
        growth = soup.find('div', class_ = 'D(ib) Mend(20px)').findAll('span')[1].text
        print(Symbol + ':', price, growth)
    except AttributeError:
        print('You have an invalid stock symbol. Try putting in one that exists.')