import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser as dParser
import matplotlib.dates as mplDates

grill = readings[335:388]

plt.subplot(111)
plt.plot_date(x=grillTimes,y=grillWatts,xdate=True)
x
oven = readings[61:172]
microwave = readings[652:671]
tv = readings[723:841]
washingMachine = readings[1092:1710]
dishWasher = readings[1818:2097]
toaster = readings[9:29]

apps = ['grill','oven','microwave',
       'tv','washingMachine','dishWasher',
       'toaster']

"""
for a in apps:
    i = apps.index(a)
    plt.subplot(231+i)
    eval('plt.plot(' + a + ')')
    plt.title(a)
"""
plt.show()

import matplotlib as mpl
import datetime as dt
import matplotlib.pyplot as plt
import re


def prepareData(fileName):
    readings = getReadings(fileName)
    readings = csvToList(readings)
    readings = convertTimes(readings)
    return readings

def buildGraph(readings):
    times = getTimes(readings)
    watts = getWatts(readings)

    # start building the graph:

    fig = plt.figure()

    graph = fig.add_subplot(111)
    graph.plot_date(x=times,y=watts,fmt='r-')

    timeFmt = mpl.dates.DateFormatter('%M:%S')  # formatting for x axis
    graph.xaxis.set_major_formatter(timeFmt)
    minLoc = mpl.dates.MinuteLocator()
    secLoc = mpl.dates.SecondLocator(interval=6)
    graph.xaxis.set_major_locator(minLoc)
    graph.xaxis.set_minor_locator(secLoc)
    
    graph.set_xlabel('Time')
    graph.set_ylabel('Watts')
    
    graph.set_title('Grill Readings')
    plt.grid(True)
    
    # rotates and right aligns the x labels, and movees bottom of axes up to make room
    fig.autofmt_xdate() #  bottom=0.18)    # adjust for date labels
    # fig.subplots_adjust(left=0.18)


readings = prepareData('grill.csv')
buildGraph(readings)
plt.savefig("grill.png")
#plt.show()
