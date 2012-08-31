"""
This module provides functions for plotting the data

"""

"""
grill = readings[335:388]
oven = readings[61:172]
microwave = readings[652:671]
tv = readings[723:841]
washingMachine = readings[1092:1710]
dishWasher = readings[1818:2097]
toaster = readings[9:29]
"""

"""
apps = ['grill','oven','microwave',
       'tv','washingMachine','dishWasher',
       'toaster']

for a in apps:
    i = apps.index(a)
    plt.subplot(231+i)
    eval('plt.plot(' + a + ')')
    plt.title(a)

plt.plot_date(x=grillTimes,y=grillWatts,xdate=True)
plt.show()
"""
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import re



import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser as dParser
import matplotlib.dates as mplDates
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

def zeroIndexTimesAxis(readings):
    """
    Zero indexes a list of times. 
    Purpose: graph starts from time 0 instead of when readings started.  
    (A better implementation would perhaps use min UTC but had probs with this.)

    Function assumes and only makes sense if readings take place within a single day

    >>>
    >>>

    """
    time0 = readings[0][0]                                              # get first reading
    d0 = time0.strftime(format=DATETIMEFORMAT)[:10] + "T00:00:00"  # set d0 to beg of day
    d0 = dt.datetime.strptime(d0,DATETIMEFORMAT)
    d1 = time0
    delta = d1 - d0
    return [[time[0] - delta, time[1]] for time in readings]


def printPlot(fileName):

    fig = plt.figure()
    graph = fig.add_subplot(111)   # neccessary?

    graph.plot_date(time,watts,marker='o',markersize=0,markeredgewidth=0,linestyle='-')

    timeFmt = mpl.dates.DateFormatter('%H:%M')
    graph.xaxis.set_major_formatter(timeFmt)
    hourLoc = mpl.dates.HourLocator(interval=3)
    #minLoc = mpl.dates.MinuteLocator(interval=15)
    graph.xaxis.set_major_locator(hourLoc)
    #graph.xaxis.set_minor_locator(minLoc)

    print('I am going to print')

    plt.show()


def buildGraph(readings):
    """
    
    """
    times = [r[0] for r in readings]
    watts = [r[1] for r in readings]

    fig = plt.figure()
    graph = fig.add_subplot(111)
    graph.plot_date(x=times,y=watts,fmt='-')

    
def saveGraph(readings,fName):
    buildGraph(readings)
    plt.savefig(fName)

def showGraph(readings):
    buildGraph(readings)
    plt.show()
