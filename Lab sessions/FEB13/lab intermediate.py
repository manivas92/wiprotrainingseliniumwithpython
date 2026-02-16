import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()

for user in users:
    print(user["username"].upper())

import requests
from requests.exceptions import Timeout

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print(response.status_code)

except Timeout:
    print("Request timed out!")

import requests

session = requests.Session()

# First request
response1 = session.get("https://httpbin.org/cookies/set/sessioncookie/123456")

# Second request (cookie persists)
response2 = session.get("https://httpbin.org/cookies")

print("Cookies:", response2.json())


import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

with open("posts.json", "w") as f:
    json.dump(posts, f, indent=4)

print("Saved to posts.json")
