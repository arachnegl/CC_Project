import numpy as np
import matplotlib.pyplot as plt
import dateutil.parser as dParser
import matplotlib.dates as mplDates

# import the smooting algos at some point


readings = np.loadtxt('appliance_study_data.csv',
                      delimiter=',',unpack=False,
                      dtype={'names':('time','watt'),
                             'formats':('S19','S4')}
                      )

"""
# Alternatively: (dflt dtype is float)
time,watts = np.loadtxt(fName,unpack=True,
                        converters={0:mpl.dates.strpdate2num('%Y-%m-%dT%H:%M:%S')},
                        delimiter=',')

"""

readings = [r for r in readings if not r[1]=='[]']    # strip out empty reads
readings = [(dParser.parse(r[0]),r[1]) for r in readings]  # str to datetime objs
readings = [(mplDates.date2num(r[0]),r[1]) for r in readings]  # conv datetime to mpl time
# alt:
#mplDateParser = mplDates.strpdate2num('%Y-%m-%dT%H:%M:%S') # if you know the str format
#readings = [(mplDateParser(r[0]),r[1] for r in readings]

# print(readings[0]) # rtrns  (734724.4361805556, '84')

times = [r[0] for r in readings]
watts = [r[1] for r in readings]

grill = readings[335:388]

plt.subplot(111)
plt.plot_date(x=grillTimes,y=grillWatts,xdate=True)

oven = readings[61:172]
microwave = readings[652:671]
tv = readings[723:841]
washingMachine = readings[1092:1710]
dishWasher = readings[1818:2097]
toaster = readings[9:29]

apps = ['grill','oven','microwave',
       'tv','washingMachine','dishWasher',
       'toaster']

"""
for a in apps:
    i = apps.index(a)
    plt.subplot(231+i)
    eval('plt.plot(' + a + ')')
    plt.title(a)
"""
plt.show()

