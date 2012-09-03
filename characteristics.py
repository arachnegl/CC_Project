"""
This module contains various characteristics of predicates and related appliances


"""

import datetime as dt
import matplotlib.dates as mdates
import numpy as np

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

# lunch -> oven; grill; toaster  @time 12:00-14:00

def getTimeSlice(begHr,endHr,readings):
    """
    returns list of values between beg and end in readings
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
    # (readings are floats so should work with conv)
    #check intensity

    #check convolve
    conv = np.convolve(grill,readings,'valid')
    detected = conv.argmax()
    if detected > 1000 : 
        return True
    else:
        return False


def isLunch(readings):
    """
    returns True or False if detects either an oven, grill or toaster

    """
    lunchPeriod = getTimeSlice(12,14,readings)
    if containsTimeSliceAppliance(lunchPeriod,grill):
        return True
    


# breakfast -> toaster           @time 7:00-9:00

# dinner -> oven; grill          @time 19:00-21:00

# fluctuations -> variations (more than one peak in histogram)

# day_low ->  small variations   @time 9:00-17:00

# night_low -> small variations  @time 24:00-8:00


import doctest
doctest.testmod()
