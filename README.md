# PSFLKPrototypRESTFlask
Installierte Pakete
linting: pylint
framework: flask mit flask-restful
Datenmanipulation: pandas

requirements:
'''pip install flask flask_restful pip pandas'''

Zum starten der api nach dem klonen:
python3 app.py

Zum ausprobieren der api, nach dem Start des Servers:
python3 test.py

Zum testen der eingebauten auth middleware(authentication_middleware.py) in der friedhofstandort.py,
sind die mit zu übergebenen Daten oben in der authentication_middleware.py zu finden

Beschreibung:
Mit dieser in Flask geschriebenen API kann auf 4 csv Dateien der Stadt Münster zugegriffen werden.
