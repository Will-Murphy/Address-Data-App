from flask import Flask, request

from address_service_wrapper import AddressServiceWrapper
from flask_cors import CORS

app = Flask(__name__)
address_service = AddressServiceWrapper(config = "./address_service_config.cfg")
CORS(app)

@app.route('/')
def hello():
    return "Welcome to the Address Data App Backend!"


@app.route('/geocode', methods=['GET'])
def geocode_one(): 
    address = request.args.get('address')
    return address_service.geocode_one(address)



@app.route('/validate', methods=['GET'])
def validate_one():
    address = request.args.get('address')
    #return address_service.validate_one(address)
    return "validate address Test"


#TODO: removed parammeters for testing 
@app.route('/validate-geocode', methods=['GET'])
def validate_and_geocode_one():
    address = request.args.get('address')
    return address_service.validate_and_geocode_one(address)


@app.route('/reverse-geocode', methods=['GET'])
def reverse_geocode_one():
    coordinates = request.args.get('coordinates')
    result = address_service.reverse_geocode_one(coordinates)
    return result




