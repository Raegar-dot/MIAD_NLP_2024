#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment_LD import predict_genre
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='Movie Genre API',
    description='Movie Genres Prediction API Team 22')

ns = api.namespace('predict', 
     description='Movies Genre Classifier')
   
parser = api.parser()

parser.add_argument(
    'year', 
    type=str, 
    required=True, 
    help="Release Year", 
    location='args')

parser.add_argument(
    'title', 
    type=str, 
    required=True, 
    help='Movie`s Title', 
    location='args')

parser.add_argument(
    'plot', 
    type=str, 
    required=True, 
    help='Movie`s synopsis', 
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
         "result": predict_genre(args['year'],args['title'],args['plot'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
