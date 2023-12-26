import requests
url = "https://www.google.co.uk/"
response = requests.get(url)
print(type(response))

print(response.status_code)
print(response.reason)