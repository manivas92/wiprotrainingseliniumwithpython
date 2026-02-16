import requests
try:

    response = requests.delete("https://videogamedb.uk:443/api/v2/videogame",)
    print(response)

    if response.status_code == 403:
        print("Status code is 403 ok")
        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print (f"An error occured {e}")