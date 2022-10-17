from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd

#Initialize the flask App
app=Flask(__name__)
#Wrap the app in api
api=Api(app)

#Adding reqparse for better access on the flask.request
#object revisit later when necessary put ecetara
#WohnberechtigteBev_

class WohnberechtigteBev(Resource):
    def __init__(self):
        #read csv file
        self.data = pd.read_csv('Wohnberechtigte-Bevölkerung-Export-bis-2020.csv',sep=';')
    def get(self, raum, zeit):
        #retreiving specified resource
        result = self.data.loc[(self.data['RAUM'] == raum)
        & (self.data['ZEIT'] == zeit)].to_json(orient="index")
        return jsonify({'message': result})
    


#adding the resource to the api and setting URL Route
api.add_resource(WohnberechtigteBev, '/wohnberechtigteBev/<string:raum>/<string:zeit>/')
#Main function for running the flask application
if __name__ == '__main__':
    app.run(debug=True)
