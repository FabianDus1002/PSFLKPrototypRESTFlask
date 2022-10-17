import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE  + "wohnberechtigteBev/12 Überwasser/31.12.1999")

print(response.json())