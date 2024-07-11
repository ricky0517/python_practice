import requests

para = {
    "lat": 43.65,
    "lon": -23.21
}
response = requests.get("http://api.open-notify.org/iss-now.json", params= para)
print(response.status_code)
print(response.json())
