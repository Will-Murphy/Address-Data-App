from flask import Flask, jsonify, request
#from flask_cors import CORS

from address_microservice.src import main_stream as addr_service_stream
from address_microservice.src import main_batch as addr_service_batch

ADDR_SERVICE_CONFIG = "./address_microservice/config.cfg" 
VALIDATE_AND_GEOCODE = "0"
VALIDATE = "1"
GEOCODE = "2"
REVERSE_GEOCODE = "3"
     
app = Flask(__name__)
#CORS(app)


@app.route('/geocode')
def geocode(): 
    args = {
        'options': GEOCODE,  
        'config': ADDR_SERVICE_CONFIG,
        'input': '31 Carey Circle, Canton, MA'
    }

    address_coordinates = addr_service_stream.run(args)
    return address_coordinates

@app.route('/')
def validate():
    return "hi"


