# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class Normalization(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
	    endpoint = 'https://identity-service-4sl6.onrender.com/v1/normalization-rules'
	    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYW5kaWRhdGUiOiJ2YWRpcmFqLTExOCIsImV4cCI6MTY3NTI3NDQwMH0.807lcqzie3f5d-BoLjdTJ3xMVPo201GqZ60ZjjlOgrI"}
	    return requests.get(endpoint, headers=headers).json()
		# return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Identities(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
	    endpoint = 'https://identity-service-4sl6.onrender.com/v1/identities'
	    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYW5kaWRhdGUiOiJ2YWRpcmFqLTExOCIsImV4cCI6MTY3NTI3NDQwMH0.807lcqzie3f5d-BoLjdTJ3xMVPo201GqZ60ZjjlOgrI"}
	    return requests.get(endpoint, headers=headers).json()
		# return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201



class ApplyNormalization(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
	    endpoint_normalization = 'https://identity-service-4sl6.onrender.com/v1/normalization-rules'
	    endpoint_identities = 'https://identity-service-4sl6.onrender.com/v1/identities'
	    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYW5kaWRhdGUiOiJ2YWRpcmFqLTExOCIsImV4cCI6MTY3NTI3NDQwMH0.807lcqzie3f5d-BoLjdTJ3xMVPo201GqZ60ZjjlOgrI"}
	    response_id = requests.get(endpoint_identities, headers=headers).json()

	    response_norm = requests.get(endpoint_normalization, headers=headers).json()
	    for rule in response_norm:
		    if len(rule["source"]["apply"]) == 0:
			    source_name = rule["source"]["name"]
			    source_field = rule["source"]["field"]
			    target_name = rule["target"]["name"]
			    target_field = rule["target"]["field"]

	    return jsonify({'Source': source_name})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201

# adding the defined resources along with their corresponding urls
api.add_resource(Identities, '/v1/identities')
api.add_resource(Normalization, '/v1/normalization-rules')
api.add_resource(ApplyNormalization, '/v1/unifiedidentities')


# driver function
if __name__ == '__main__':

	app.run(debug = True)

