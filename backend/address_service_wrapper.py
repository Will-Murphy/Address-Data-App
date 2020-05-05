from address_microservice.src import main_stream as addr_service_stream
from address_microservice.src import main_batch as addr_service_batch

"""
Wrapper Functions around address microservice to provide directly callable 
access to its functionality 
"""

# File path for config file relative to cwd
ADDR_SERVICE_CONFIG = "./address_microservice/config.cfg" 

# Options codes for address microservice
VALIDATE_AND_GEOCODE = "0"
VALIDATE = "1"
GEOCODE = "2"
REVERSE_GEOCODE = "3"


def validate_one(address):
    args = {
        'options': VALIDATE,
        'config': ADDR_SERVICE_CONFIG,
        'input': address
    }
    validated_address = addr_service_stream.run(args)
    return validated_address


def validate_and_geocode_one(address):
    args = {
        'options': VALIDATE_AND_GEOCODE,  
        'config': ADDR_SERVICE_CONFIG,
        'input': address
    }
    validated_and_geocoded_address = addr_service_stream.run(args)
    return validated_and_geocoded_address


def geocode_one(address): 
    args = {
        'options': GEOCODE,  
        'config': ADDR_SERVICE_CONFIG,
        'input': address
    }
    address_coordinates = addr_service_stream.run(args)
    return address_coordinates 


def reverse_geocode_one(coordinates): 
    args = {
        'options': GEOCODE,  
        'config': ADDR_SERVICE_CONFIG,
        'input': coordinates
    }
    address = addr_service_stream.run(args)
    pass