'''
In der Datei app.py werden die URL-endpoints der API definiert.
Zusätzlich wird die Flask-App und die API iniziiert
'''
from flask import Flask
from flask_restful import Api
from resources.migration import Migration
from resources.wohnberechtigte import WohnberechtigteBev
from resources.babyhitliste import BabyHitliste
from resources.friedhofstandort import FriedhofStandort

#Initialize the flask App
app=Flask(__name__)
#Wrap the app in api
api=Api(app)

#adding the resources with specified URLs to the api
api.add_resource(WohnberechtigteBev, '/wohnberechtigteBev/<string:raum>/<string:zeit>')
api.add_resource(BabyHitliste, '/babyhitliste/<int:jahr>/<int:rang>/<string:geschlecht>')
api.add_resource(FriedhofStandort, '/friedhofstandort/<string:name>')
api.add_resource(Migration, '/migration/<string:zeit>/<string:raum>/<string:merkmal>')
#Main function for running the flask application
if __name__ == '__main__':
    app.run(debug=True)
