from flask import Flask, abort, request
from flask_restful import Resource, Api, reqparse
import pandas as pd

#Adding reqparse for better access on the flask.request
wohnberechtigte_post_args = reqparse.RequestParser()
wohnberechtigte_post_args.add_argument("ZEIT", type=str, help='Datum des Eintrages ist erforderlich', required=True)
wohnberechtigte_post_args.add_argument("RAUM", type=str, help='Der Raum für den Eintrag ist erforderlich', required=True)
wohnberechtigte_post_args.add_argument("MERKMAL", type=str, help='Merkmal des Eintrags ist erforderlich', required=True)
wohnberechtigte_post_args.add_argument("WERT", type=str, help='Wert des Eintrags ist erforderlich', required=True)

class WohnberechtigteBev(Resource):
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('Wohnberechtigte-Bevölkerung-Export-bis-2020.csv',sep=';')
    def get(self, raum, zeit):
        #retreiving specified resource
        result = self.data.loc[(self.data['RAUM'] == raum)
        & (self.data['ZEIT'] == zeit)].to_json(orient="index")
        return result, 200
    def post(self, raum, zeit):
        #parser to paste the data from the request
        args = wohnberechtigte_post_args.parse_args()
        print(args)
        #Wenn ein Eintrag mit dem übergebenen Zeitraum und Raum existiert, soll kein neuer erstellt werden. 
        #if (((self.data['RAUM'] == args.RAUM).any()) and ((self.data['ZEIT'] == args.ZEIT).any())):
        #    abort(409)
        #else:
        self.data=self.data.append(args, ignore_index=True)
        self.data.to_csv('Wohnberechtigte-Bevölkerung-Export-bis-2020.csv', index=False)
        return 201
    def put():
        return ""
    def patch():
        return ""
    def delete(self, raum, zeit):
        return
    