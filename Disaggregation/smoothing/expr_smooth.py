import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

def stripEmptyReadings(aFile):
    """
    Strips empty readings marked as watt readings of '[]' from a current cose data file
    """
    readings = []
    with open(aFile,'r') as f:
        readings = f.readlines()
    f.close()

    # if '[]' not found, findall rtrns [] which is equivalent to False
    readings = [r for r in readings if not re.findall(r",\[\]",r)]

    with open(aFile,'w') as f:
        for r in readings:
            f.write("{}".format(r))  # using py3 syntax
    f.close()


def extractReadings(aFile):
    """
    extracts readings from a file in format [[float,int]]
    (float represents time in matplotlib dates)
    """
    readings = np.loadtxt(aFile,delimiter=',',unpack=False,
                          dtype={'names':('time','watts'),'formats':('f12','i4')},
                          converters={0:mpl.dates.strpdate2num('%Y-%m-%dT%H:%M:%S'),1:int} )

    return readings


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
