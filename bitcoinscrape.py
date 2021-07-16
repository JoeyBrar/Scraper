import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Go to our selected URL with a browser, get its page source, store it in a readible format and then quit the browser:
driver = webdriver.Chrome(executable_path = '/Users/jorabrar/Downloads/chromedriver') 
driver.get('https://www.google.com/search?q=bitcoin+price&rlz=1C5CHFA_enUS943US943&oq=bitcoin+price&aqs=chrome.0.69i59j69i60.1587j0j7&sourceid=chrome&ie=UTF-8')  
results = [] 
content = driver.page_source 
soup = BeautifulSoup(content, 'lxml') 
driver.quit()

# Gets data from the parsed source and puts it in our list
for count in soup.findAll(class_ ='dDoNo ikb4Bb gsrt gzfeS'):
    price = count.find('span')
    
    if price not in results:
        results.append(price.text)

df = pd.DataFrame({'One Bitcoin (in USD): ' : results})
df.to_csv('Bitcoin.csv', index = False, encoding = 'utf-8')
print('The bitcoin price per one bitcoin is $' + results[0] + ' USD')