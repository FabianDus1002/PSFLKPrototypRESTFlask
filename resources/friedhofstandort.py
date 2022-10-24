'''
In firedhofstandort.py wird die Klasse Friedhofstandort für die korrespondierende Ressource angelegt
und die benötigten Methoden implementiert. Zur Nutzung von Daten die in der Query übergeben werden
die requestParser von flask_restful verwendet
'''
import flask
from flask_restful import Resource, reqparse, abort
import pandas as pd
from authentication_middleware import authfunc

#argument parser to collect data from post and put request
post_put_args = reqparse.RequestParser()
post_put_args.add_argument('NAME', type=str, help='Name des Eintrags ist erforderlich...',
 required=True)
post_put_args.add_argument('RECHTSWERT', type=int,
 help='Rechtswert des Eintrags ist erforderlich...', required=True)
post_put_args.add_argument('HOCHWERT', type=int , help='Hochwert des Eintrags ist erforderlich...',
required=True)
post_put_args.add_argument('HOMEPAGE', type=str, help='Homepage des Eintrags ist erforderlich...',
required=True)

#since not all arguments are required for patch, there is a need for a second argument parser
patch_args = reqparse.RequestParser()
patch_args.add_argument('NAME', type=str, help='Name des Eintrags ist erforderlich...')
patch_args.add_argument('RECHTSWERT', type=int, help='Rechtswert des Eintrags ist erforderlich...')
patch_args.add_argument('HOCHWERT', type=int , help='Hochwert des Eintrags ist erforderlich...')
patch_args.add_argument('HOMEPAGE', type=str, help='Homepage des Eintrags ist erforderlich...')

class FriedhofStandort(Resource):
    '''
    In der Klasse FriedhofStandort, werden die HTTP-Methoden
    get, post, put, patch und delete definiert,
    die für die Interaktion mit FriedhofStandorte.csv benötigt werden
    '''
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('data/FriedhofStandorte.csv',sep=',')
    
    def get(self, name):
        '''Mit get wird die JSON Repräsentation der spezifizierte Ressource aus der csv angefragt'''
        result = self.data.loc[(self.data['NAME'] == name)]
        if result.empty:
            abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
            return None

        response = flask.make_response(result.to_json(orient="records"))
        response.headers['content-type'] = 'application/json'
        return response

    @authfunc
    def post(self, name):
        '''Mit post wird eine neue Ressource in der csv angelegt'''
        result = self.data.loc[(self.data['NAME'] == name)]
        #check if there is a resource under specified URI
        if result.empty:
            #retrieving args
            args = post_put_args.parse_args()
            self.data=self.data.append(args, ignore_index=True)
            self.data.to_csv('data/FriedhofStandorte.csv', index=False)

            return 201

        abort(405, message="Es gibt schon einen Eintrag unter der spezifizierten Ressource")
        return None

    @authfunc
    def put(self, name):
        '''Mit put wird eine spezifizierte Ressource in der csv aktualisiert'''
        result = self.data.loc[(self.data['NAME'] == name)]
        #check if there is a resource under specified URI
        if result.empty:
            abort(404, message="Es ist kein Eintrag mit diesen Daten verfügbar...")
        else:
            args = post_put_args.parse_args()
            self.data.loc[self.data['NAME'] == name] = [args['NAME'], args['RECHTSWERT'],
             args['HOCHWERT'], args['HOMEPAGE']]
            self.data.to_csv('data/FriedhofStandorte.csv', index=False)

    @authfunc
    def patch(self, name):
        '''Mit patch wird eine spezifizierte Ressource in der csv partiell aktualisiert'''
        result = self.data.loc[(self.data['NAME'] == name)]
        #check if there is a resource under specified URI
        if result.empty:
            abort(404, message="Es ist kein Eintrag mit diesen Daten verfügbar...")
        else:
            args = patch_args.parse_args()
            if args['NAME']:
                self.data.loc[(self.data['NAME'] == name), ['NAME']] = args['NAME']
            if args['RECHTSWERT']:
                self.data.loc[(self.data['NAME'] == name), ['RECHTSWERT']] = args['RECHTSWERT']
            if args['HOCHWERT']:
                self.data.loc[(self.data['NAME'] == name), ['HOCHWERT']] = args['HOCHWERT']
            if args['HOMEPAGE']:
                self.data.loc[(self.data['NAME'] == name), ['HOMEPAGE']] = args['HOMEPAGE']
            self.data.to_csv('data/FriedhofStandorte.csv', index=False)

    @authfunc
    def delete(self, name):
        '''delete löscht die spezifizierte Ressource aus der csv'''
        result = self.data.loc[(self.data['NAME'] == name)]
        if not result.empty:
            self.data = self.data.drop(self.data.loc[(self.data['NAME'] == name)].index)
            self.data.to_csv("data/FriedhofStandorte.csv", index=False)
            return "",200

        abort(404, message="Kein Eintrag mit diesen Daten verfügbar...")
        return None
