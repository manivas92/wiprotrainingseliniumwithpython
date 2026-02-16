from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com"
headers = {

    "User-Agent": "Edge/5.0"
}

response = requests.get(url, headers = headers)
print(response.status_code)

soup = BeautifulSoup(response.text, features="html.parser")
print(soup)

print(soup.title.string)

print(soup.find("h1"))

print(soup.find("p"))

books = soup.find_all("article", class_ = "product_pod")

for book in books:
    tittle = book.find("h3").find("a")["title"]
    price = book.find("p",class_="price_color").text
    print("title",tittle)
    print("price",price)
