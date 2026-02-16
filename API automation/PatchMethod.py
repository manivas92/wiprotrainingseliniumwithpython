import requests
try:
    data ={
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
   }

    response = requests.patch("https://videogamedb.uk:443/api/v2/videogame/ff8081819c5368bb019c55a4c6060473", json = data)
    print(response)

    if response.status_code == 200:
        print("Status code is 200 ok")
        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print (f"An error occured {e}")