import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("-" * 30)

import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}

response = requests.get(url, params=params)

posts = response.json()
print("Number of posts:", len(posts))

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "New Post",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)

if response.status_code == 201:
    print("Resource created successfully")

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception("Request failed!")

print("Success")
