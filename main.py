from app import *

def __main__():
    print(f"::: SERVER RUNNING :::\n")
    app.run(host="0.0.0.0",port=app_port,debug=app_debug_mode)
    
__main__()