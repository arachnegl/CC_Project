"""
Provides plotting functions for current cost data

Usage:
    fig = getTimeWattFigure(readings,'myGraphTitle')
    fig.show()
    fig.savefig('nameOfFile')

"""


import matplotlib.pyplot as plt

import timeutils_cc as tu    # for zeroIndexTimesAxisMPL
import appldata_cc as ap      # for app graphing func

import numpy as np    # for smooth function

def getConvolveFigure(convVals,readings):
    """
    line plot
    """
    idxmax = convVals.argmax()
    

    fig = plt.figure()

    ax1 = fig.add_subplot(211)
    ax1.plot(convVals,'b-')
    ax1.axvline(idxmax,linewidth=1,color='r')
    ax1.set_title('convolution')
    ax1.grid(True)

    idxmaxMPLtime = readings[idxmax][0]

    ax2 = fig.add_subplot(212)
    rdTs = getTimes(readings)
    rdWs = getWatts(readings)
    ax2.plot_date(rdTs,rdWs,fmt='b-')
    ax2.axvline(idxmaxMPLtime,linewidth=1,color='r')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Watts')
    ax2.grid(True)

    return fig

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



def getTimeWattFigure(readings,name='Time Series Plot Of Watts',zeroed=False):
    """
    Returns straightforward time series of watt values
    
    """
    if zeroed:
        readings = tu.zeroIndexTimesAxisMPL(readings)

    times = getTimes(readings)
    watts = getWatts(readings)

    fig = plt.figure()

    axs = fig.add_subplot(111)
    axs.plot_date(x=times,y=watts,fmt='b-')
    axs.set_xlabel('Time')
    axs.set_ylabel('Watts')
    
    axs.set_title(name)
    axs.grid(True)
    
    # rotates and right aligns the x labels, and movees bottom of axes up to make room
    fig.autofmt_xdate() #  bottom=0.18)    # adjust for date labels
    # fig.subplots_adjust(left=0.18)
    return fig

def getAnalysisTimeWattFigure(readings,name):

    pdng = 2  # padding value

    readings = tu.zeroIndexTimesAxisMPL(readings)
    fig = getTimeWattFigure(readings,name)

    # additions:
    axs = fig.get_axes()[0]
    appWatts = getWatts(readings)
    maxApp = max(appWatts[pdng:-pdng])
    minApp = min(appWatts[pdng:-pdng])

    axs.hlines(maxApp,readings[pdng][0],readings[-pdng][0],color='r')
    axs.hlines(minApp,readings[pdng][0],readings[-pdng][0],color='r')

    xs = getTimes(readings)
    axs.fill_between(xs,appWatts,facecolor='0.8')

    axs.set_ylim(0,2300)
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

def smooth(x,window_len=11,window='hanning'):
    """smooth the data using a window with requested size.

    (taken from: www.scipy.org/Cookbook/SignalSmooth)
    """

    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"


    s=np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    return y


def getSmoothFigure(appl,title='Different Smoothing Algorithms'):

    x = [0 for i in range(15)]
    xx= [w[1] for w in appl] 
    x = x + xx + x                  # add some 'padding' either side of data
    x = np.array(x)
   
    fig = plt.figure()
    axs = fig.add_subplot(111)
    
    yorg = x
    yflt = smooth(x,5,'flat')
    yhan = smooth(x,5,'hanning')
    yham = smooth(x,5,'hamming')
    ybrt = smooth(x,5,'bartlett')
    yblk = smooth(x,5,'blackman')

    org,flt,han,ham,brt,blk  = axs.plot( yorg,'b-',
                                         yflt,'g-',
                                         yhan,'r-',
                                         yham,'c-',
                                         ybrt,'m-',
                                         yblk,'y-')
    

    axs.legend( (org,flt,han,ham,brt,blk),
                ('original', 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'),
                fancybox=True,
                shadow=True)
   
    axs.set_ylim(0,3500)
    axs.set_ylabel('Watts')
    axs.set_title(title)

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
