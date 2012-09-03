"""
Script to print graph of days 3 at a time (for now)

You probably only want to issue this cmd to get imgs of all files:
    filesOfAllDaysWithOver12kReadings()

(any file that contains less than 12k readings is almost certainly incomplete - ie. not a full day)

Typical usage:
    files = getListOfFiles(insertPath)
    days = getAllReadings(files)
    threeDays = getFigureWithGraphsOf(days[:3])

"""
import cc_io as io
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def getListOfFiles(path):
    fNames = os.listdir(path)
    fNames = sorted(fNames)
    fNames = [path + fn for fn in fNames]
    return fNames

def getAllReadings(fList):
    allReadings = []
    for f in fList:
        allReadings.append(io.getReadingsFromFile(f))

    return allReadings

def getFigureWithGraphsOf(readings):
    fig = plt.figure()

    nmbrGraphs = len(readings)

    for i in range(nmbrGraphs):
        times = io.getTimes(readings[i])
        watts = io.getWatts(readings[i])

        # graph is axis instance rtrnd by fig.add_subplot
        graph = fig.add_subplot(nmbrGraphs,1,i)
        graph.plot_date(x=times,y=watts,fmt='b-')
        graph.set_xlabel('Time')
        graph.set_ylabel('Watts')
 
        # Naming - use date of first reading for name:
        day = mdates.num2date(readings[i][0][0])
        dayName = day.strftime('%A %d %B %Y')
        graph.set_title(dayName)
        
        formatter = mdates.DateFormatter('%H')
        graph.xaxis.set_major_formatter(formatter)

        graph.grid(True)

    #fig.autofmt_xdate()

    return fig


def filesOfAllDayFigures(pathToFiles='../CC_Captures/cleanCCdata/'):
    files = getListOfFiles(pathToFiles)
    days = getAllReadings(files)

    # I should have 24 files, discarding partial 1st and last = 22    (7*3 =21) 7 graphs!!

    for i in [1,4,7,10,13,16,19]:
        graph = getFigureWithGraphsOf(days[i:i+3])
        graph.savefig('pics/fig' + str(i))

def filesOfAllDaysWithOver12kReadings(pathToFiles='../CC_Captures/cleanCCdata/'):
    files = getListOfFiles(pathToFiles)
    days = getAllReadings(files)

    days = [d for d in days if len(d) > 12000]

    for i in [1,4,7,10,13,16]:
        graph = getFigureWithGraphsOf(days[i:i+3])
        graph.savefig('pics/fig' + str(i))
