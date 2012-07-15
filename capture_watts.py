#!/usr/bin/python

import serial, re, time, csv
from datetime import datetime, date, time

# There should be a try here, see pyserial doc
connection = serial.Serial(port = '/dev/ttyUSB0',
                           baudrate = 57600,
                           timeout = 3)

date = datetime.now().date()  # date is obj, state gets updated later.
outFile = csv.writer(open(date.isoformat() + '_cc.csv','w'))

while True:
    reading = connection.readline()

    print("This reading was found:")
    print(reading)

    if reading == '':
        continue

    # NB type of watts changes dynamically
    # re.findall rtrns a list, we always want first element
    # hope is that polling will be frequent enough to get data as it arrives

        outFile.writerow([datetime.now().time().isoformat()[:8]
                      ,watts])



def extract_watts(reading):
    watts = re.findall(r"<watts>[0-9]{5}</watts>",reading)
    if watts == []:
        print("this reading contains no watts - skipping to next reading.")
        return -1
    else:
        watts = watts[0]
        watts = re.findall(r"[0-9]{5}",watts)[0]
        watts = int(watts)
        return watts


#    time.sleep(2)


#    time = re.findall(r"<time>[0-9]{2}:[0-9]{2}:[0-9]{2}</time>",reading)[0]
#    time = re.findall(
#    time = time.split(':')
#    hour = time[0]
#    min = time[1]
#    sec = time[2]
