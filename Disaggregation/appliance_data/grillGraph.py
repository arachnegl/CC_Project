import matplotlib as mpl
import datetime as dt
import matplotlib.pyplot as plt
import re

def getReadings(fileName):
    """
    returns file contents as list of lines 
    """
    with open(fileName,'r') as f:
        return [r for r in f.readlines()]

def csvToList(csvList):
    """
    ['2012-09-07T12:01:02,211'] -> [['2012-09-07T12:01:02','211']]

    csv parser better than below - but wanted to experiment)
    """
    readings = [r[0:-2] for r in csvList]              # truncate newline chars
    return [re.split(r',',r,2) for r in readings]      # split str into two ',' delimiter

def convertTimes(readings):
    """
    Converts repr of time: str -> datetime objs -> matplotlib times
    
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)
    """
    readings = [[dt.datetime.strptime(r[0],"%Y-%m-%dT%H:%M:%S"),r[1]] for r in readings]
    readings = zeroIndexTimesAxis(readings)                                 # zero index the time values
    return [[mpl.dates.date2num(r[0]),r[1]] for r in readings]   # convert to mpl dates (floats)


def zeroIndexTimesAxis(readings):
    """
    Zero indexes a list of times. 
    Purpose: graph starts from time 0 instead of when readings started.  
    (A better implementation would perhaps use min UTC but had probs with this.)

    Function assumes and only makes sense if readings take place within a single day
    """
    time0 = readings[0][0]                                              # get first reading
    d0 = time0.strftime(format="%Y-%m-%dT%H:%M:%S")[:10] + "T00:00:00"  # set d0 to beg of day
    d0 = dt.datetime.strptime(d0,"%Y-%m-%dT%H:%M:%S")
    d1 = time0
    delta = d1 - d0
    return [[time[0] - delta, time[1]] for time in readings]


def getTimes(readings):
    """
    returns first column in list with 'two columns'

    eg: [[a,b]] -> [a]

    """
    return [r[0] for r in readings]

def getWatts(readings):
    """
    returns second column in list with 'two columns'

    eg: [[a,b]] -> [b]

    """
    return [r[1] for r in readings]

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
