import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-newsfeed"

querystring = {"category":"generalnews","region":"US"}

headers = {
	"x-rapidapi-key": "00c4aad806msh8e00931585a4552p1cba4fjsn25893b3ff1c5",
	"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())