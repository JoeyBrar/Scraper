import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/Users/jorabrar/Downloads/chromedriver')
driver.get('https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI')
price = []
growth = []
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
driver.quit()

for a in soup.findAll(class_ = 'D(ib) Mend(20px)'):
    pr = a.find('span')
    if pr not in price:
        price.append(pr.text)

for b in soup.findAll(attrs = 'D(ib) Mend(20px)'):
    gr = b.find('span', {'class' : 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'})
    if gr not in growth:
        growth.append(gr.text)

df = pd.DataFrame({'Dow Jones Industrial Average:' : price, 'Growth:' : growth})
df.to_csv('Dow30.csv', index = False, encoding = 'utf-8')

print('The average of 30 companies is $' + price[0] + ' USD (' + growth[0] + ')')
