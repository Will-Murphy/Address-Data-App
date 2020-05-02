#!/bin/bash
export FLASK_APP=./backend/app.py
source env/bin/activate
flask run -h 0.0.0.0


## To Run 
#chmod u+x bootstrap.sh
#./bootstrap.sh &