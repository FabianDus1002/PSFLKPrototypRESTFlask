# PSFLKPrototypRESTFlask
Installierte Pakete
linting: pylint
framework: flask mit flask-restful
Datenmanipulation: pandas

requirements:
'''pip install flask flask_restful pandas'''

Zum starten der api nach dem klonen:
python3 app.py

Zum ausprobieren der api, nach dem Start des Servers:
python3 test.py

Zum testen der eingebauten auth middleware(authentication_middleware.py) in der friedhofstandort.py,
sind die mit zu übergebenen Daten oben in der authentication_middleware.py zu finden.
Die Middleware ist nicht ausreichend sicher und soll nur zeigen, wie eine Middleware in Flask implementiert
werden kann.

Beschreibung:
Mit dieser in Flask geschriebenen API kann auf 4 csv Dateien der Stadt Münster zugegriffen werden.
Die Dateien sind die folgenden:
-MuensterBabyHitListe
    -Enthält die Vornamensstatistik der Jahre 2007–2021
    -Datenspalten:
        -Jahr: Geburtsjahr
        -Rang: Top 30 Rang
        -Geschlecht: Mädchen oder Junge
        -Name: Der gewählte Name
        -Anzahl: Anzahl Kinder mit diesem Namen
    -Link: https://opendata.stadt-muenster.de/dataset/vornamenstatistik-f%C3%BCr-neugeborene-nach-geburtsjahr-m%C3%BCnster/resource/3b6ef14a-d308-407c-8dd4#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}}}

-Migration
    -Enthält Informationen über die Migrationsdaten der Stadt Münster
    -Datenspalten:
        -JAHR: Jahr
        -RAUM: Viertel der Stadt Münster
        -MERKMAL Ausländer, Deutsche mit persönlicher Migrationsvorgeschichte, 
                Deutsche mit vererbter Migrationsvorgeschichte, Deutsche ohne erkennbare Migrationsvorgeschichte
        -WERT: Anzahl von Merkmalsträgern
    -Link: https://opendata.stadt-muenster.de/dataset/bev%C3%B6lkerungsindikatoren-migration/resource/614bf467-9781-485d-b1e8-440a9dae1736#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}}}

-FriedhofStandorte
    -Enthält die Standortkoordinaten (Gauß-Krüger-Koordinatensystem) von Friedhöfen der Stadt Münster und die dazugehörigen Webadressen
    -Datenspalten:
        -NAME: Name des Friedhofs
        -RECHTSWERT: Rechtswert Koordinate des Friedhofs
        -HOCHWERT: Hochwert Koordinate des Friedhofs
        -HOMEPAGE: Homepage des Friedhofs
     -Link: https://opendata.stadt-muenster.de/dataset/friedhof-standorte/resource/0e871fbf-2310-4b2d-905b-229d9bb6fb00

-Wohnberechtige Bevoelkerung 
    -Enthält Informationen über die Wohnberechtigte Bevölkerung der Stadt Münster von 1999–2020
    -Datenspalten:
        -ZEIT: Stichtag des Eintrags
        -RAUM: Stadtteil
        -MERKMAL: "Wohnberechtigte Bevölkerung"
        -WERT: Anzahl
    -Link: https://opendata.stadt-muenster.de/dataset/wohnberechtigte-bev%C3%B6lkerung-pro-stadtteil-im-verlauf/resource/6e4613aa-280a-466d-ac06#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}}}