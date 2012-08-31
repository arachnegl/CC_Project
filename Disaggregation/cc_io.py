"""
This module defines various input functions for parsing and loading readings from cc files

It also includes some functions for cleaning the data and extracting watts and times arrays

Finally it also provides some time related functions
"""
import numpy as np
from matplotlib.dates import strpdate2num as mpl_strpdate2num
from matplotlib.dates import date2num as mpl_date2num
import datetime as dt

# defines string date format for date parsers
DATETIMEFORMAT = '%Y-%m-%dT%H:%M:%S'


def extractValuesFromCCFile(ccFile):
    """
    Returns values from current cost csv file as numpy array (list of tuples)
    eg. [('2012-07-22T00:00:18','79')...] 

    """
    readings = np.loadtxt(ccFile,
                      delimiter=',',unpack=False,
                      dtype={'names':('time','watt'),  # dtype is not used but good practice
                             'formats':('S19','S4')}
                      )
    return readings




def removeNonDigitReadings(readings):
    """
    removes all readings which have a non digit watt value

    >>> r = [('2012-01-01T00:00:00','84'),('2013-08-01T01:01:01','[]')]
    >>> removeNonDigitReadings(r)
    [('2012-01-01T00:00:00', '84')]

    """
    #readings = [r for r in readings if not r[1]=='[]']    # works in practice but not general enough
    readings = [r for r in readings if r[1].isdigit()]
    return readings


def stripEmptyReadings(aFile):
    """
    Strips empty readings marked as watt readings of '[]' from a current cose data file
    it then saves over-writing original file
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


def convertStrDateTimesToMPLDateTimes(readings):
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

    mplDateParser = mpl_strpdate2num(DATETIMEFORMAT)      # strpdate2num seems undocumented except in src code
    readings = [(mplDateParser(r[0]),r[1]) for r in readings]
    return readings


def convertStrDateTimesToMPLDateTimes2(readings):
    """
    Converts repr of time: str -> datetime objs -> matplotlib times
    
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)
    
    Alternative for convertStrDateTimesToMPLDateTimes as strpdate2num 
    seems undocumented except in source code (is it deprecated?)

    >>> r = [('2012-01-01T00:00:00','84')]
    >>> convertStrDateTimesToMPLDateTimes2(r)
    [(734503.0, '84')]
    """
    readings = [(dt.datetime.strptime(r[0],DATETIMEFORMAT),r[1]) for r in readings]
    return [(mpl_date2num(r[0]),r[1]) for r in readings]   # convert to mpl dates (floats)


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


def getReadingsFromFile(ccFile):
    """
    Wrapper around functions above 

    """
    readings = extractValuesFromCCFile(ccFile)
    readings = removeNonDigitReadings(readings)
    readings = convertStrDateTimesToMPLDateTimes(readings)
    return readings


import doctest
doctest.testmod()
