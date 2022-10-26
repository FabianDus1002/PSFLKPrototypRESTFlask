'''
In der test.py Datei, werden die Methoden für die 4 definierten Ressourcen,
-babyhitliste.py
-friedhofstandort.py
-migration.py
-wohnberechtigte.py
getestet
'''
import requests

BASE = "http://127.0.0.1:5000/"

response =requests.get(BASE  + "babyhitliste/2007/1/Junge", timeout=5)
print(response.json())
input()

response =requests.delete(BASE  + "babyhitliste/2022/1/Junge", timeout=5)
print(response.json())
input()
#with the appended JSON String data can be send via the request
response = requests.post(BASE  + "babyhitliste/2022/1/Junge",
 {"Jahr":2022, "Rang":1, "Geschlecht":"Junge", "Name":"Fabian","Anzahl":23} , timeout=5)

print(response.json())

input()

response = requests.put(BASE + "babyhitliste/2022/1/Junge",
 {"Jahr":2022, "Rang":1, "Geschlecht":"Junge", "Name":"Peter","Anzahl":23}, timeout=5)
print(response.json)

input()

response = requests.patch(BASE + "babyhitliste/2022/1/Junge", {"Anzahl":24}, timeout=5)
#with the variabele auth, authentication data can be send via the request
response = requests.delete(BASE + "friedhofstandort/Friedhof H1", timeout=5, auth=('test1','testTest'))
print(response.json())
input()
response =requests.get(BASE  + "friedhofstandort/Friedhof Kinderhaus", timeout=5, auth=('test1','testTest'))
print(response.json())

input()
response = requests.post(BASE  + "friedhofstandort/Friedhof H1",
{"NAME":"Friedhof H1", "RECHTSWERT":1, "HOCHWERT":"2", "HOMEPAGE":"example.com"}, timeout=5, auth=('test1','testTest'))
print(response.json())

input()
response = requests.put(BASE  + "friedhofstandort/Friedhof H1",
 {"NAME":"Friedhof H1", "RECHTSWERT":2, "HOCHWERT":3, "HOMEPAGE":"example.com"}, timeout=5, auth=('test1','testTest'))
print(response.json())

input()
response = requests.patch(BASE  + "friedhofstandort/Friedhof H1", {"HOCHWERT":34}, timeout=5, auth=('test1','testTest'))
print(response.json())

input()
response = requests.post(BASE + "wohnberechtigteBev/11 Aegidii/31.12.2023",
 {"ZEIT":"31.12.2023", "RAUM":"11 Aegidii", "MERKMAL":"Test", "WERT":1}, timeout=5)
print(response.json())

input()
response = requests.get(BASE + "wohnberechtigteBev/11 Aegidii/31.12.2023", timeout=5)
print(response.json())

input()
response = requests.put(BASE  + "wohnberechtigteBev/11 Aegidii/31.12.2023",
 {"ZEIT":"31.12.2023", "RAUM":"11 Aegidii", "MERKMAL":"Test", "WERT":2}, timeout=5)
print(response.json())

input()
response = requests.patch(BASE + "wohnberechtigteBev/11 Aegidii/31.12.2023", {"WERT":3}, timeout=5)
print(response.json())

input()
response = requests.delete(BASE + "wohnberechtigteBev/11 Aegidii/31.12.2023", timeout=5)
print(response.json())

input()
response = requests.post(BASE + "migration/31.12.2022/11 Aegidii/Ausländer",
{"ZEIT":"31.12.2022", "RAUM":"11 Aegidii", "MERKMAL":"Ausländer", "WERT":82}, timeout=5)
print(response.json())

input()
response = requests.get(BASE + "migration/31.12.2022/11 Aegidii/Ausländer", timeout=5)
print(response.json())

input()
response = requests.put(BASE + "migration/31.12.2022/11 Aegidii/Ausländer",
 {"ZEIT":"31.12.2022", "RAUM":"11 Aegidii", "MERKMAL":"Ausländer", "WERT":83}, timeout=5)
print(response.json())

input()
response = requests.patch(BASE + "migration/31.12.2022/11 Aegidii/Ausländer",
 {"WERT":84}, timeout=5)

input()
response = requests.delete(BASE + "migration/31.12.2022/11 Aegidii/Ausländer", timeout=5)
print(response.json())
