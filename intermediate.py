from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

names=soup.find_all("a",class_="title")
desc=soup.find_all("p",class_="description")
prices=soup.find_all("h4",class_="price float-end card-title pull-right")
product_name=[]
product_price=[]
description=[]
for i in names:
    name=i.text
    product_name.append(name)
#print(product_name)

for i in desc:
    dec=i.text
    description.append(dec)
#print(description)


for i in prices:
    price=i.text
    product_price.append(price)
#print(product_price)

df=pd.DataFrame({"product_name":product_name,"product_price":product_price,"Description":description})
print(df)


