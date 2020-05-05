from flask import Flask, request

from address_service_wrapper import AddressServiceWrapper
#from flask_cors import CORS

app = Flask(__name__)
address_service = AddressServiceWrapper(config = "./address_microservice/config.cfg")
#CORS(app)

@app.route('/')
def hello():
    return "Welcome to the Address Data App!"


@app.route('/geocode/<string:address>')
def geocode_one(address): 
    return address_service.geocode_one(address)


@app.route('/validate/<string:address>')
def validate_one(address):
    return address_service.validate_one(address)


#TODO: removed parammeters for testing 
@app.route('/validate-geocode/<string:address>')
def validate_and_geocode_one(address):
    return address_service.validate_and_geocode_one(address)


@app.route('/reverse-geocode/<string:coordinates>')
def reverse_geocode_one(coordinates):
    return address_service.reverse_geocode_one(coordinates)




