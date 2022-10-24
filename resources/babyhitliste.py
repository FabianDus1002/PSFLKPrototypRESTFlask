'''
In babyhitliste.py wird die Klasse BabyHitliste für die korrespondierende Ressource angelegt
und die benötigten Methoden implementiert. Zur Nutzung von Daten die in der Query übergeben werden
die requestParser von flask_restful verwendet
'''
import flask
from flask_restful import Resource, reqparse, abort
import pandas as pd

#argument parser to collect data from post and put request
post_put_arg = reqparse.RequestParser()
post_put_arg.add_argument('Jahr', type=int, help='Jahr des Eintrags ist erforderlich',
 required=True)
post_put_arg.add_argument('Rang', type=int, help='Rang des Eintrags ist erforderlich',
 required=True)
post_put_arg.add_argument('Geschlecht', type=str, help='Geschlecht des Eintrags ist erforderlich',
 required=True)
post_put_arg.add_argument('Name', type=str, help='Name des Eintrags ist erforderlich',
 required=True)
post_put_arg.add_argument('Anzahl', type=int, help='Anzahl des Eintrags ist erforderlich',
 required=True)

#since not all arguments are required for patch, there is a need for a second argument parser
patch_arg = reqparse.RequestParser()
patch_arg.add_argument('Jahr', type=int, help='Jahr des Eintrags ist erforderlich')
patch_arg.add_argument('Rang', type=int, help='Rang des Eintrags ist erforderlich')
patch_arg.add_argument('Geschlecht', type=str, help='Geschlecht des Eintrags ist erforderlich')
patch_arg.add_argument('Name', type=str, help='Name des Eintrags ist erforderlich')
patch_arg.add_argument('Anzahl', type=int, help='Anzahl des Eintrags ist erforderlich')

class BabyHitliste(Resource):
    '''
    In der Klasse Babyhitliste, werden die HTTP-Methoden
    get, post, put, patch und delete definiert,
    die für die Interaktion mit MuensterBabyHitliste.csv benötigt werden
    '''
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('data/MuensterBabyHitliste.csv',sep=',')
    def get(self, jahr, rang, geschlecht):
        '''Mit get wird die JSON Repräsentation der spezifizierte Ressource aus der csv angefragt'''
        #retreiving specified resource
        result = self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)]
        if not result.empty:
            response = flask.make_response(result.to_json(orient="records"))
            response.headers['content-type'] = 'application/json'
            return response

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None

    def post(self, jahr, rang, geschlecht):
        '''Mit post wird eine neue Ressource in der csv angelegt'''
        #check if there is a ressource with specified data
        result = self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)]
        if result.empty:
            #retrieving args
            args = post_put_arg.parse_args()
            self.data=self.data.append(args, ignore_index=True)
            self.data.to_csv('data/MuensterBabyHitliste.csv', index=False)

            return "",201

        abort(405, message="Es gibt schon einen Eintrag unter der spezifizierten Ressource")
        return None

    def put(self, jahr, rang, geschlecht):
        '''Mit put wird eine spezifizierte Ressource in der csv aktualisiert'''
        #check if there is a ressource with specified data
        result = self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)]
        if result.empty:
            abort(404, message="Es ist kein Eintrag mit diesen Daten verfügbar...")
        else:
            put_args=post_put_arg.parse_args()
            self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)] = [put_args['Jahr'],
                 put_args['Rang'], put_args['Geschlecht'], put_args['Name'], put_args['Anzahl']]
            self.data.to_csv('data/MuensterBabyHitliste.csv', index=False)

    def patch(self, jahr, rang, geschlecht):
        '''Die Methode patch wird zum partiellen modifizieren einer Ressource
            in der MuensterBabyHitliste.csv verwendet
        '''
        result = self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)]
        if result.empty:
            abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        else:
            #parse args
            args = patch_arg.parse_args()
            if args['Jahr']:
                self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht), ['Jahr']] = args['Jahr']
            if args['Rang']:
                self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht), ['Rang']] = args['Rang']
            if args['Geschlecht']:
                self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht), ['Geschlecht']] = args['Geschlecht']
            if args['Name']:
                self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht), ['Name']] = args['Name']
            if args['Anzahl']:
                self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht), ['Anzahl']] = args['Anzahl']
            self.data.to_csv('data/MuensterBabyHitliste.csv', index=False)

    def delete(self, jahr, rang, geschlecht):
        '''delete löscht die spezifizierte Ressource aus der MuensterBabyHitliste.csv'''
        result = self.data.loc[(self.data['Jahr'] == jahr)
                & (self.data['Rang'] == rang)
                & (self.data['Geschlecht'] == geschlecht)]
        if not result.empty:
            self.data = self.data.drop(self.data.loc[(self.data['Jahr'] == jahr)
                                    & (self.data['Rang'] == rang)
                                    & (self.data['Geschlecht'] == geschlecht)].index)
            self.data.to_csv("data/MuensterBabyHitliste.csv", index=False)
            return "",200

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None
                 