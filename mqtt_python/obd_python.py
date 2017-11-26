import obd

connection = obd.Async() # auto-connects to OBD2

_TEMP
if(connection.status()):

    speed = obd.commands.SPEED # speed values
    oil_temp = obd.commands.OIL_TEMP #oil temp

    connection.watch(speed) #keeps track async of SPEED
    connection.watch(oil_temp) #keeps track async of OIL
    # send the command, and parse the response
    connection.start()

    print(str(connection.query(speed))) # returns unit-bearing values thanks to Pint
    print(str(connection.query(oil_temp))) # user-friendly unit conversions
