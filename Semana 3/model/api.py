#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment import predict_price
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='Car Price API',
    description='Car Price Prediction API Team 22')

ns = api.namespace('predict', 
     description='Car Price Regressor')
   
parser = api.parser()

parser.add_argument(
    'year', 
    type=str, 
    required=True, 
    help="Car's build year", 
    location='args')

parser.add_argument(
    'mileage', 
    type=str, 
    required=True, 
    help='Mileage of the car', 
    location='args')

parser.add_argument(
    'state', 
    type=str, 
    required=True, 
    help='US State where the car is located', 
    location='args')

parser.add_argument(
    'make', 
    type=str, 
    required=True, 
    help="Car's Brand", 
    location='args')

parser.add_argument(
    'model', 
    type=str, 
    required=True, 
    help="Car's Model", 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_price(args['year'],args['mileage'],args['state'],args['make'],args['model'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
