#!/bin/bash
export FLASK_APP=./backend/app.py
source backend/bin/activate
python -m flask run -h 0.0.0.0


##  To Run 
# chmod u+x backend.sh
# ./backend.sh & ( & to run in backround)

##  Kill Script running in backround 
# kill -9  <pid> 
