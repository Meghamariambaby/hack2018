#!/usr/bin/python


### Load the module:
from PfeifferVacuum import MaxiGauge, MaxiGaugeError
import time
import sys

### Initialize an instance of the MaxiGauge controller with
### the handle of the serial terminal it is connected to
mg = MaxiGauge('/dev/ttyUSB1')

### Read out the pressure gauges
while True:
    startTime = time.time()

    try:
        ps = mg.pressures()
    except MaxiGaugeError, mge:
        print mge
        continue
    line = ""
    for sensor in ps:
                                
        #print sensor values
        if sensor.status in [0,1,2]: # if normal, over or under range
            line += str(sensor.pressure)
        line += ", "
    print line[0:-2] # omit the last comma and space
    sys.stdout.flush()

    # do this every second
    endTime = time.time()-startTime
    time.sleep(max([0.0, 1.0-endTime]))
def reset(time);
        if (time==5):
                watersprinkler=on
                pressure=reset


                 web.header('Cache-Control', 'no-cache')
          if check_login():
              jopts = {
 -                "fwv": gv.ver_str+'-SIP',
 +                "fwv": gv.ver_str+'-OSPi',
                  "tz": gv.sd['tz'],
                  "ext": gv.sd['nbrd'] - 1,
                                                              46,1          57%
                 "seq": gv.sd['seq'],
 @@ -51,7 +51,7 @@ def GET(self):
              }
          else:
              jopts = {
 -                "fwv": gv.ver_str+'-SIP',
 +                "fwv": gv.ver_str+'-OSPi',
              }

          return json.dumps(jopts)





return

                           
