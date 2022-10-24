'''
In migration.py wird die Klasse Migration für die korrespondierende Ressource angelegt
und die benötigten Methoden implementiert. Zur Nutzung von Daten die in der Query übergeben werden
die requestParser von flask_restful verwendet
'''
import flask
from flask_restful import Resource, reqparse, abort
import pandas as pd

#argument parser to collect data from post and put request
post_put_args = reqparse.RequestParser()
post_put_args.add_argument("ZEIT", type=str, help='Datum des Eintrages ist erforderlich',
 required=True)
post_put_args.add_argument("RAUM", type=str, help='Der Raum für den Eintrag ist erforderlich',
 required=True)
post_put_args.add_argument("MERKMAL", type=str, help='Merkmal des Eintrags ist erforderlich',
 required=True)
post_put_args.add_argument("WERT", type=int, help='Wert des Eintrags ist erforderlich',
 required=True)

#since not all arguments are required for patch, there is a need for a second argument parser
patch_args = reqparse.RequestParser()
patch_args.add_argument("ZEIT", type=str, help='Datum des Eintrages ist erforderlich')
patch_args.add_argument("RAUM", type=str, help='Der Raum für den Eintrag ist erforderlich')
patch_args.add_argument("MERKMAL", type=str, help='Merkmal des Eintrags ist erforderlich')
patch_args.add_argument("WERT", type=int, help='Wert des Eintrags ist erforderlich')

class Migration(Resource):
    '''
    In der Klasse Migration, werden die HTTP-Methoden
    get, post, put, patch und delete definiert,
    die für die Interaktion mit Migration.csv benötigt werden
    '''
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('data/Migration.csv',sep=',')
    def get(self, zeit, raum, merkmal):
        '''Mit get wird die JSON Repräsentation der spezifizierte Ressource aus der csv angefragt'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
        & (self.data['RAUM'] == raum)
        & (self.data['MERKMAL'] == merkmal)]
        if not result.empty:
            response = flask.make_response(result.to_json(orient="records"))
            response.headers['content-type'] = 'application/json'
            return response

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None

    def post(self, zeit, raum, merkmal):
        '''Mit post wird eine neue Ressource in der csv angelegt'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)
                & (self.data['MERKMAL'] == merkmal)]
        if result.empty:
            args = post_put_args.parse_args()
            self.data=self.data.append(args, ignore_index=True)
            self.data.to_csv('data/Migration.csv', index=False)
            return "",201
        abort(405, message="Es gibt schon einen Eintrag unter der spezifizierten Ressource")
        return None

    def put(self, zeit, raum, merkmal):
        '''Mit put wird eine spezifizierte Ressource in der csv aktualisiert'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)
                & (self.data['MERKMAL'] == merkmal)]
        if result.empty:
            abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        else:
            args = post_put_args.parse_args()
            self.data.loc[((self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum))] = [args['ZEIT'], args['RAUM']
                                                , args['MERKMAL'], args['WERT']]
            self.data.to_csv("data/Migration.csv", index=False)

    def patch(self,zeit,raum,merkmal):
        '''Mit patch wird eine spezifizierte Ressource in der csv partiell aktualisiert'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)
                & (self.data['MERKMAL'] == merkmal)]
        if result.empty:
            abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        else:
            #parse args
            args = patch_args.parse_args()
            if args['RAUM']:
                self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum), ['RAUM']] = args['RAUM']
            if args['ZEIT']:
                self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum), ['ZEIT']] = args['ZEIT']
            if args['MERKMAL']:
                self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum), ['MERKMAL']] = args['MERKMAL']
            if args['WERT']:
                self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum), ['WERT']] = args['WERT']

            self.data.to_csv("data/Migration.csv", index=False)

    def delete(self, zeit, raum, merkmal):
        '''delete löscht die spezifizierte Ressource aus der csv'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)
                & (self.data['MERKMAL'] == merkmal)]
        if not result.empty:
            self.data = self.data.drop(self.data.loc[(self.data['ZEIT'] == zeit)
                                    & (self.data['RAUM'] == raum)
                                    & (self.data['MERKMAL'] == merkmal)].index)
            self.data.to_csv("data/Migration.csv", index=False)
            return "",200
        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None
