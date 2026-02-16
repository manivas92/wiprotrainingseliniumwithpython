import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)

data = html.fromstring(response.content)

title = data.find(".//title").text
print(title)

links = data.xpath("//a/@href")
print(links)

links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))

response = requests.get(url, timeout=10)
tree = html.fromstring(response.content)
titles = tree.xpath("//span[@class='titleline']/a/text()")
for t in titles:
    print(t)