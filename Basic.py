from bs4 import BeautifulSoup
import requests
url="https://webscraper.io/test-sites"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

tag=soup.header
print(tag.attrs["role"])

String=soup.div.p.string
print(String)

