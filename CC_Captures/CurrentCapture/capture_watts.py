#!/usr/bin/python

import serial, re, time, csv, os, sys
from datetime import datetime

# There should be a try here, see pyserial doc
try:
    connection = serial.Serial(port = '/dev/ttyUSB0',
                           baudrate = 57600,
                           timeout = 5)
except SerialException:
    print("Device not found or not configured")
    print("Program exiting now!")
    sys.exit(-1)

# assuming filename unique from timestamp down to seconds
outFile = csv.writer(open(datetime.now().isoformat()[:19] + '_cc.csv','w'))

while True:
    reading = connection.readline()

    if reading == '':
        continue

    print("Reading found:")
    print(reading)

    # NB type of watts changes dynamically
    # re.findall rtrns a list, we always want first element
    watts = re.findall(r"<watts>[0-9]{5}</watts>",reading)
    if watts == []:
        print("No watts, skipping reading")
    else:
        watts = watts[0]
        watts = re.findall(r"[0-9]{5}",watts)[0]
        watts = int(watts)
    
    dnt = datetime.now().isoformat()[:19]
    outFile.writerow([dnt,watts])
