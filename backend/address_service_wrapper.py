from address_microservice.src import main_stream as addr_service_stream
from address_microservice.src import main_batch as addr_service_batch

"""
Wrapper Functions around address microservice to provide directly callable 
access to its functionality 
"""

class AddressServiceWrapper():

    # Options codes for address microservice
    VALIDATE_AND_GEOCODE = "0"
    VALIDATE = "1"
    GEOCODE = "2"
    REVERSE_GEOCODE = "3"
 
    def __init__(self, path_to_config):
        self.config = path_to_config # path to config fromcwd where wrapper used

    def validate_one(self, address):
        """ stream address validation """
        args = {
            'options': self.VALIDATE,
            'config': self.config,
            'input': address
        }
        validated_address = addr_service_stream.run(args)
        return validated_address


    def validate_and_geocode_one(self, address):
        """ stream address validation & geocoding """
        args = {
            'options': self.VALIDATE_AND_GEOCODE,  
            'config': self.config,
            'input': address
        }
        validated_and_geocoded_address = addr_service_stream.run(args)
        return validated_and_geocoded_address


    def geocode_one(self, address): 
        """ stream address geocoding """
        args = {
            'options': self.GEOCODE,  
            'config': self.config,
            'input': address
        }
        address_coordinates = addr_service_stream.run(args)
        return address_coordinates 


    def reverse_geocode_one(self, coordinates): 
        """ stream address reverse geocoding """
        args = {
            'options': self.REVERSE_GEOCODE,  
            'config': self.config,
            'input': coordinates
        }
        address = addr_service_stream.run(args)
        return address