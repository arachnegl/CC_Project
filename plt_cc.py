"""
This module provides functions for plotting the data



"""


import matplotlib.pyplot as plt

import timeUtils as tu    # for zeroIndexTimesAxisMPL
import appData as ap      # for app graphing func



def getTimes(readings):
    """
    returns first column in list with 'two columns'

    eg: [[a,b]] -> [a]

    >>> a = [('12-08-12',345),('12-08-13',123)]
    >>> getTimes(a)
    ['12-08-12', '12-08-13']
    """
    return [r[0] for r in readings]


def getWatts(readings):
    """
    returns list of watt values from second column of inputted list

    [(a,b)] -> [b]

    >>> a = [('12-08-12',345),('12-08-13',123)]
    >>> getWatts(a)
    [345, 123]
    """
    return [r[1] for r in readings]



def getTimeWattFigure(times,watts,name):
    """
    Returns straightforward time series of watt values
    
    """
    fig = plt.figure()

    axs = fig.add_subplot(111)
    axs.plot_date(x=times,y=watts,fmt='r-')
    axs.set_xlabel('Time')
    axs.set_ylabel('Watts')
    
    axs.set_title(name)
    axs.grid(True)
    
    # rotates and right aligns the x labels, and movees bottom of axes up to make room
    fig.autofmt_xdate() #  bottom=0.18)    # adjust for date labels
    # fig.subplots_adjust(left=0.18)
    return fig



def getAppFig():
    """
    Returns figure showing all appliances

    cmds:
    f = getAppFig1()
    f.savefig('appliances.png')

    (I know there is a better way of doing this)
    """
    # grill
    grRs = ap.grill
    grRs = tu.zeroIndexTimesAxisMPL(grRs)
    grTs = getTimes(grRs)
    grWs = getWatts(grRs)

    # oven
    ovRs = ap.oven
    ovRs = tu.zeroIndexTimesAxisMPL(ovRs)
    ovTs = getTimes(ovRs)
    ovWs = getWatts(ovRs)
    
    # microwave
    mwRs = ap.microwave
    mwRs = tu.zeroIndexTimesAxisMPL(mwRs)
    mwTs = getTimes(mwRs)
    mwWs = getWatts(mwRs)

    # tv
    tvRs = ap.tv
    tvRs = tu.zeroIndexTimesAxisMPL(tvRs)
    tvTs = getTimes(tvRs)
    tvWs = getWatts(tvRs)

    # toaster
    tsRs = ap.toaster
    tsRs = tu.zeroIndexTimesAxisMPL(tsRs)
    tsTs = getTimes(tsRs)
    tsWs = getWatts(tsRs)

    # washing machine
    wmRs = ap.washingMachine
    wmRs = tu.zeroIndexTimesAxisMPL(wmRs)
    wmTs = getTimes(wmRs)
    wmWs = getWatts(wmRs)

    # dish washer
    dwRs = ap.dishWasher
    dwRs = tu.zeroIndexTimesAxisMPL(dwRs)
    dwTs = getTimes(dwRs)
    dwWs = getWatts(dwRs)


    fig = plt.figure(figsize=None)

    ax1 = fig.add_subplot(211)
    ax1.set_title('Rectangular-like appliance signatures')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Watts')
    ax1.xaxis_date(tz=None)

    gr,ov,mw,tv = ax1.plot( grTs,grWs,'b-',    # rtrns 2D line
                            ovTs,ovWs,'g-',
                            mwTs,mwWs,'r-',
                            tvTs,tvWs,'c-')

    ax1.legend( (gr,ov,mw,tv),           # 2Dline handles
                ('Grill','Oven','Microwave','Television'),
                loc=('upper right'),
                fancybox=True,
                shadow=True)
    
    ax2 = fig.add_subplot(212)
    ax2.set_title('Periodic-like  appliance signatures')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Watts')
    ax2.xaxis_date(tz=None)

    ts,wm,dw = ax2.plot( tsTs,tsWs,'m-',
                         wmTs,wmWs,'g-',
                         dwTs,dwWs,'r-')
             
    ax2.legend( (ts,wm,dw),           # 2Dline handles
                ('Toaster','Washing Machine','Dishwasher'),
                loc=('upper right'),
                fancybox=True,
                shadow=True)
    
    fig.subplots_adjust(hspace=0.5)
    #fig.autofmt_xdate()   # erases x-axis of second graph
    return fig



"""
# unneeded (for now) formatting code:
timeFmt = mpl.dates.DateFormatter('%M:%S')  # formatting for x axis
graph.xaxis.set_major_formatter(timeFmt)
minLoc = mpl.dates.MinuteLocator()
secLoc = mpl.dates.SecondLocator(interval=6)
graph.xaxis.set_major_locator(minLoc)
graph.xaxis.set_minor_locator(secLoc)
"""
