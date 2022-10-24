'''
In wohnberechtigte.py wird die Klasse WohnberechtigteBev für die korrespondierende Ressource
angelegt
und die benötigten Methoden implementiert. Zur Nutzung von Daten die in der Query übergeben werden
die requestParser von flask_restful verwendet
'''
import flask
from flask_restful import Resource, reqparse, abort
import pandas as pd

#Adding reqparse for better access on the flask.request object
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


class WohnberechtigteBev(Resource):
    '''
    In der Klasse WohnberechtigteBev, werden die HTTP-Methoden
    get, post, put, patch und delete definiert,
    die für die Interaktion mit Wohnberechtigte-Bevoelkerung.csv benötigt werden
    '''
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('data/Wohnberechtigte-Bevoelkerung.csv',sep=',')
    def get(self, raum, zeit):
        '''Mit get wird die JSON Repräsentation der spezifizierte Ressource aus der csv angefragt'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)]
        if not result.empty:
            response = flask.make_response(result.to_json(orient="records"))
            response.headers['content-type'] = 'application/json'
            return response

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None

    def post(self, raum, zeit):
        '''Mit post wird eine neue Ressource in der csv angelegt'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)]
        if result.empty:
            args = post_put_args.parse_args()
            self.data=self.data.append(args, ignore_index=True)
            self.data.to_csv('data/Wohnberechtigte-Bevoelkerung.csv', index=False)
            return "",201
        abort(405, message="Es gibt schon einen Eintrag unter der spezifizierten Ressource")
        return None

    def put(self, raum, zeit):
        '''Mit put wird eine spezifizierte Ressource in der csv aktualisiert'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
            & (self.data['RAUM'] == raum)]
        if result.empty:
            abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        else:
            args = post_put_args.parse_args()
            self.data.loc[((self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum))] = [args['ZEIT'], args['RAUM'],
                 args['MERKMAL'], args['WERT']]
            self.data.to_csv("data/Wohnberechtigte-Bevoelkerung.csv", index=False)

    def patch(self, raum, zeit):
        '''Mit patch wird eine spezifizierte Ressource in der csv partiell aktualisiert'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)]
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

            self.data.to_csv("data/Wohnberechtigte-Bevoelkerung.csv", index=False)

    def delete(self, raum, zeit):
        '''delete löscht die spezifizierte Ressource aus der csv'''
        result = self.data.loc[(self.data['ZEIT'] == zeit)
                & (self.data['RAUM'] == raum)]
        if not result.empty:
            self.data = self.data.drop(self.data.loc[(self.data['ZEIT'] == zeit)
                                    & (self.data['RAUM'] == raum)].index)
            self.data.to_csv("data/Wohnberechtigte-Bevoelkerung.csv", index=False)
            return "",200

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None
