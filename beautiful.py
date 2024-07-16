from bs4 import  BeautifulSoup
import requests

web="https://subslikescript.com/movie/Titanic-120338"

result=requests.get(web)
#print(result.text)
content=result.text

soup=BeautifulSoup(content,'lxml')
#print(soup.prettify())

box=soup.find('article', class_ ='main-article')

title=box.find('h1').get_text()
print(title)

transcript=box.find('div',class_='full-script').get_text(strip=True,separator=' ')
print(transcript)

with open('titanic.txt','w') as file:
    file.write(transcript)



