"""
Contains variety of utility functions for 
handling time and time axis in readings

DateTimes are handled differently according to python or matplotlib
creates need to translate between the two.

    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)

Also plotting data from time zero requires translation.

"""

import datetime as dt
import matplotlib.dates as mdates

# defines string date format for date parsing
DATETIMEFORMAT = '%Y-%m-%dT%H:%M:%S'


def zeroIndexTimesAxisDT(readings):
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
    return [(time[0] - delta, time[1]) for time in readings]


def zeroIndexTimesAxisMPL(readings):
    """
    Zero indexes a reading's list of mpl datetimes
    """
    dt0 = mdates.num2date(readings[0][0])
    dt0 = dt0.isoformat()
    dt0 = dt0[:10] + "T00:00:00"
    dt0 = dt.datetime.strptime(dt0,DATETIMEFORMAT)
    d1 = mdates.num2date(readings[0][0])
    d1 = d1.replace(tzinfo=None)
    # dt0.replace(tzinfo=None)
    delta = d1 - dt0
    # import pdb; pdb.set_trace()
    results = [(mdates.num2date(r[0]).replace(tzinfo=None),r[1]) for r in readings]
    results = [(r[0] - delta, r[1]) for r in results]
    return [(mdates.date2num(r[0]),r[1]) for r in results]


def convertStrDateTimesToMPLDateTimes(readings):
    """
    Converts repr of time: str -> datetime objs -> matplotlib times
    
    Alternative for convertStrDateTimesToMPLDateTimes as strpdate2num 
    seems undocumented except in source code (is it deprecated?)

    >>> r = [('2012-01-01T00:00:00','84')]
    >>> convertStrDateTimesToMPLDateTimes2(r)
    [(734503.0, '84')]
    """
    readings = [(dt.datetime.strptime(r[0],DATETIMEFORMAT),r[1]) for r in readings]
    return [(mdates.date2num(r[0]),r[1]) for r in readings]   # convert to mpl dates (floats)



def convertStrDateTimesToMPLDateTimes2(readings):
    """
    converts string datetimes into datetimes suitable for matplotlib's date_plot function
    
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)
    
    NB: strpdate2num seems undocumented except in source code 
    convertStrDatetimesToMPLDateTimes2 which circumvents use of this function
    is available in case it is deprecated

    >>> r = [('2012-01-01T00:00:00','84')]
    >>> convertStrDateTimesToMPLDateTimes(r)
    [(734503.0, '84')]
    """
    # Alternative:
    # readings = [(dParser.parse(r[0]),r[1]) for r in readings]      # str to datetime objs
    # readings = [(mplDates.date2num(r[0]),r[1]) for r in readings]  # conv datetime to mpl time

    mplDateParser = mdates.strpdate2num(DATETIMEFORMAT)      # strpdate2num seems undocumented except in src code
    readings = [(mplDateParser(r[0]),r[1]) for r in readings]
    return readings


"""
Various tools to synthesise days

"""


def dayRange():
    start = dt.datetime(2012,01,01,0,0,0)  # take minum time as arbitrary beg
    for n in range((60*60*24)/6):
        yield start + dt.timedelta(seconds = 6*n)


def getMPLDatesDayRange(interval):
    start = dt.datetime(2012,01,01,0,0,0)
    end = start + dt.timedelta(days=1)
    return mdates.drange(start,end,dt.timedelta(seconds=6))
