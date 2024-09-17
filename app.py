from flask import Flask
from pyconn import Pyconn

######################################
#                                    #
#           Configuration            #
#                                    #
######################################
app=Flask(__name__)
app_port=8000
app_debug_mode=True
# database path
db=Pyconn("./_db/prueba.db")

######################################
#                                    #
#             Application            #
#                                    #
######################################

@app.route("/")
def index():
    return "<h1>Flasking great!</h1>"

@app.route("/finger")
def get_finger_print():
    return "<h1>You are mine, baby</h1>"