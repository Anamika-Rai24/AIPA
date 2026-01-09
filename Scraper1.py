import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
Soup = BeautifulSoup(response.text,"html.parser")

quotes = Soup.find_all("span",class_ = "text")
authors = Soup.find_all("small",class_ = "author")
print("Questes from the page :")
for q, a in zip(quotes, authors):
    print(f"{q.get_text()} - {a.get_text()}")



