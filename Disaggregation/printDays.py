"""
Script to print graph of days 3 at a time (for now)

Typical usage:
    files = getListOfFiles(insertPath)
    days = getAllReadings(files)
    threeDays = getFigureWithGraphsOf(days[:3])

"""
import cc_io as io
import os
import matplotlib.pyplot as plt

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

        graph = fig.add_subplot(nmbrGraphs,1,i)
        graph.plot_date(x=times,y=watts,fmt='r-')
        graph.set_xlabel('Time')
        graph.set_ylabel('Watts')

        # name = readings[i][0] # need to convert this to datetime then str
        graph.set_title('day' + str(i))
        graph.grid(True)

    fig.autofmt_xdate()

    return fig


