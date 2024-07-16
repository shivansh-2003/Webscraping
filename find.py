from bs4 import BeautifulSoup
import requests

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

price=soup.find("h4",{"class":"price float-end card-title pull-right"})

print(price.string)

desc=soup.find("p",class_="description card-text")
print(desc.string)

price_all=soup.find_all("h4",class_="price float-end card-title pull-right")
#print(price_all)

for i in price_all:
    print(i)

