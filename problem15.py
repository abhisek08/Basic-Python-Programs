'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''
import requests
from bs4 import BeautifulSoup
url='https://www.nytimes.com/'
r=requests.get(url)
r_text=r.text
soup=BeautifulSoup(r_text)
print(soup)