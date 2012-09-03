"""
Script to print graph of appliances

cmds:
    f = getAppFig1()
    f.savefig('appliances.png')

"""

import cc_io as io   # for getTimes and getWatts
import graphScript as gs  # for zeroIndexTimesAxisMPL
import matplotlib.pyplot as plt


listOfApp = ['grill','oven','microwave',
       'tv','washingMachine','dishWasher',
       'toaster']

appReadings = io.getReadingsFromFile('appliance_data_clean.csv')


grill = appReadings[335:388]
oven = appReadings[61:172]
microwave = appReadings[652:671]
tv = appReadings[723:841]
washingMachine = appReadings[1092:1710]
dishWasher = appReadings[1818:2097]
toaster = appReadings[9:29]

# grill
grRs = grill
grRs = gs.zeroIndexTimesAxisMPL(grRs)
grTs = io.getTimes(grRs)
grWs = io.getWatts(grRs)

# oven
ovRs = oven
ovRs = gs.zeroIndexTimesAxisMPL(ovRs)
ovTs = io.getTimes(ovRs)
ovWs = io.getWatts(ovRs)

# microwave
mwRs = microwave
mwRs = gs.zeroIndexTimesAxisMPL(mwRs)
mwTs = io.getTimes(mwRs)
mwWs = io.getWatts(mwRs)

# tv
tvRs = tv
tvRs = gs.zeroIndexTimesAxisMPL(tvRs)
tvTs = io.getTimes(tvRs)
tvWs = io.getWatts(tvRs)

# toaster
tsRs = toaster
tsRs = gs.zeroIndexTimesAxisMPL(tsRs)
tsTs = io.getTimes(tsRs)
tsWs = io.getWatts(tsRs)

# washing machine
wmRs = washingMachine
wmRs = gs.zeroIndexTimesAxisMPL(wmRs)
wmTs = io.getTimes(wmRs)
wmWs = io.getWatts(wmRs)

# dish washer
dwRs = dishWasher
dwRs = gs.zeroIndexTimesAxisMPL(dwRs)
dwTs = io.getTimes(dwRs)
dwWs = io.getWatts(dwRs)

def getAppFig1():
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
