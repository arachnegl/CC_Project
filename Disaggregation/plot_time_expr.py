import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def printPlot(fileName):
    time,watts = np.loadtxt(fileName,unpack=True,
                        converters={0:mpl.dates.strpdate2num('%Y-%m-%dT%H:%M:%S')},
                        delimiter=',')

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
