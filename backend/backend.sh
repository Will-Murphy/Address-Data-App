#!/bin/bash
export FLASK_APP=./backend/app.py
source backend/bin/activate
python -m flask run 


##   To Run 
# chmod u+x backend.sh
# ./backend.sh & ( & to run in backround)

##  Kill Script running in backround 
# pkill -9 -f <script_name> 
