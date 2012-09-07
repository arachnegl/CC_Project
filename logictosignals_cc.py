"""
This module contains various characteristics of predicates and related appliances



"""

import datetime as dt
import matplotlib.dates as mdates
import numpy as np
import plt_cc as pc


def getDate(aMPLDateTimeFloat):
    """
    returns a datetime obj containing date of 
    passed Matplotlib datetime float

    >>> getDate(734703.0000462963)
    datetime.date(2012, 7, 19)
    """
    dtObj = mdates.num2date(aMPLDateTimeFloat)
    date = dtObj.date()
    return date


def getTimeSlice(begHr,endHr,readings):
    """
    returns list of values between beg and end in readings

    need to implement case for if night reading detected (ie over midnight)
    """
    todayDate = getDate(readings[0][0])  # returns datetime object with date
    todayDateTime = dt.datetime.combine(todayDate,dt.time(0,0,0))
    beg = todayDateTime + dt.timedelta(hours=begHr)      #
    beg = mdates.date2num(beg)
    end = todayDateTime + dt.timedelta(hours=endHr)      #
    end = mdates.date2num(end)

    result = [r for r in readings if (beg < r[0]) and (r[0] < end)]
    return result

def getConvolve(appl,reading):
    """
    Wrapper function around numpy's convolve. 
    
    Provides more convenient handling.
    """
    aWatts = [w[1] for w in appl]
    rWatts = [w[1] for w in reading]

    conv = np.convolve(aWatts,rWatts,'valid')  # 'valid' means overlap is required
    return conv

def isGrillDetected(readings):
    """
    returns True if grill is found, False otherwise
    """

    # hist analysis to check existence of intensity
    histFound = False
    watts = pc.getWatts(readings)
    hist = np.histogram(watts,32,(0,3200)) # grill expected around early 3ks
    if (hist[0][31] + hist[0][30]) > 10:  # at least 10*6 = 1 min
        histFound = True
    else:
        return false

    #check convolve
    conv = np.convolve(grill,readings,'valid')
    detected = conv.argmax()
    if detected > 1000 and histFound: 
        return True
    else:
        return False


def isLunch(readings,begHr=12,endHr=13):
    """
    returns True or False if detects either an grill or toaster

    lunch -> oven; grill; toaster  @time 12:00-14:00
    """
    # no req fr hist analysis, individ appliances need to do it
    lunchPeriod = getTimeSlice(begHr,endHr,readings)

    if isGrillDetected(lunchPeriod):
        return True
    if isToasterDetected(lunchPeriod):
        return True
    return False


# fluctuations -> variations (more than one peak in histogram)




# day_low ->  small variations   @time 9:00-17:00
def isDayLow(readings,begHr=9,endHr=17):
    """
    checks if a low can be determined during day
    """
    #hist analysis to determine low vals
    dayLowPeriod=getTimeSlice(begHr,endHr,readings)
    if isLowDetected(dayLowPeriod):
        return True
    else:
        return False



# night_low -> small variations  @time 24:00-8:00
def isNightLow(readings,begHr=23,endHr=8):
    """
    checks if a low can be determined at night

    (Awaits night case impl)
    """
    #hist analysis to determine low vals

    nightLowPeriod=getTimeSlice(begHr,endHr,readings)
    if isLowDetected(nightLowPeriod):
        return True
    else:
        return False




import doctest
doctest.testmod()
