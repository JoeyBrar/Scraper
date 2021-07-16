from bs4 import BeautifulSoup
import requests

with open('/Users/jorabrar/Desktop/LearnHtml/lesson1notes.html') as html_file: # opens an html file I have
    soup = BeautifulSoup(html_file, 'lxml') # passes the html file into beautiful soup
    
    #print(soup) # prints the webscraped html code
    #print(soup.prettify()) # prints the html code we scraped in a prettier way, so its indented.

    match = soup.title # makes match equal to the title of the website 
    # print(match)
    match = soup.title.text # makes match equal to the only the TEXT of the title of the website, not including the <title> tags.
    print(match)

    body = soup.body # makes body equal to the body of the website
    #print(body)
    body = soup.body.text # makes body equal to only the TEXT of the body of the website, not the tags.
    #print(body)