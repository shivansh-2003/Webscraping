import pandas as pd
from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://ticker.finology.in/"

r=requests.get(url)
#print(r)
soup=BeautifulSoup(r.text,"lxml")
#print(soup)
table=soup.find("table",class_="table table-sm table-hover screenertable")
#print(table)
headers=table.find_all("th")

titles=[]
for i in headers:
    title=i.text
    titles.append(title)
#print(titles)
df=pd.DataFrame(columns=titles)
print(df)


