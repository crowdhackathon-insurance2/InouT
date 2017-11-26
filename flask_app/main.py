from flask import Flask
from flask import render_template
#import obd

app = Flask(__name__)

# connection = obd.Async() # auto-connects to OBD2
#
# if(connection.status()):
#
#     speed = obd.commands.SPEED # speed values
#     oil_temp = obd.commands.OIL_TEMP #oil temp
#
#     connection.watch(speed) #keeps track async of SPEED
#     connection.watch(oil_temp) #keeps track async of OIL
#     # send the command, and parse the response
#     connection.start()
#
#     print(str(connection.query(speed))) # returns unit-bearing values thanks to Pint
#     print(str(connection.query(oil_temp))) # user-friendly unit conversions



@app.route('/')
def hello_world():
    return render_template('index.html');

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
