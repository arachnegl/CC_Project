"""
This module provides functions for plotting the data

"""

import matplotlib.pyplot as plt

import dateutil.parser as dParser
import matplotlib.dates as mplDates
import datetime as dt

import matplotlib as mpl


def buildGraph(times,watts,name):
    """
    Function to build a graph
    returns the figure object
    """
    fig = plt.figure()

    graph = fig.add_subplot(111)
    graph.plot_date(x=times,y=watts,fmt='r-')
    graph.set_xlabel('Time')
    graph.set_ylabel('Watts')
    
    graph.set_title(name)
    graph.grid(True)
    
    # rotates and right aligns the x labels, and movees bottom of axes up to make room
    fig.autofmt_xdate() #  bottom=0.18)    # adjust for date labels
    # fig.subplots_adjust(left=0.18)
    return fig


def saveGraph(figObj,fName):
    # maybe add some auto time in fName from figObj?
    figObj.savefig(fName)


def showGraph(figObj):
    figObj.show()


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
    delta = d1 - d0                 # amount to be subracted from each reading
    return [[time[0] - delta, time[1]] for time in readings]




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

"""
# unneeded (for now) formatting code:
timeFmt = mpl.dates.DateFormatter('%M:%S')  # formatting for x axis
graph.xaxis.set_major_formatter(timeFmt)
minLoc = mpl.dates.MinuteLocator()
secLoc = mpl.dates.SecondLocator(interval=6)
graph.xaxis.set_major_locator(minLoc)
graph.xaxis.set_minor_locator(secLoc)
"""

