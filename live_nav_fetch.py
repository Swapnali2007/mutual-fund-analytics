import requests
url = " https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()
print(data)