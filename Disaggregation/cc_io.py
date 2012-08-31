"""
This module defines various input functions for parsing and loading readings from cc files

It also includes some functions for cleaning the data and extracting watts and times arrays

Finally it also provides some time related functions
"""
import csv, sys
import numpy as np
from matplotlib.dates import strpdate2num as mpl_strpdate2num
from matplotlib.dates import date2num as mpl_date2num
import datetime as dt

# defines string date format for date parsers
DATETIMEFORMAT = '%Y-%m-%dT%H:%M:%S'


def extractValuesFromCSV(csvFile):
    """
    Returns a list of two value lists stripping entries with no numeric values. (In practice '[]')

    Raises:
	IOError: if csvFile not found
        csv.Error: if error in csvFile
    """ 
    readings = []
    lRead = 0
    nVals = 0

    with open(csvFile, 'r') as f: 
        reader = csvReader(f)
        try:
            for line in reader:
                lRead += 1
                if line[1].isdigit():
                    nVals += 1
                    readings.append(line)
                else:   # value is '[]' so no reading, ignore
                    continue
        except csv.Error, e:
            sys.exit('file %s, line %d,: $s' % (filename, reader.line_num, e))
        else:
            print("Finished extraction. Lines read: %s Actual Readings: %s" 
                     %(lRead,nVals)) 
# probably to be added to unittests:
    if [x for x in readings if not x[1].isdigit()] == [] and len(readings) == nVals:
        return readings
    else:
        return -1


def extractValues(ccFile):
    readings = np.loadtxt(ccFile,
                      delimiter=',',unpack=False,
                      dtype={'names':('time','watt'),  # dtype is not used but good practice
                             'formats':('S19','S4')}
                      )
    return readings

    """
    # Alternatively: (dflt dtype is float)
    time,watts = np.loadtxt(fName,unpack=True,
                        converters={0:mpl.dates.strpdate2num(DATETIMEFORMAT)},
                        delimiter=',')

    """

# Yet another version:
def getReadings(fileName):
    """
    returns file contents as list of lines 
    """
    with open(fileName,'r') as f:
        return [r for r in f.readlines()]

def csvToList(csvList):
    """
    ['2012-09-07T12:01:02,211'] -> [['2012-09-07T12:01:02','211']]

    csv parser better than below - but good to experiment)
    """
    readings = [r[0:-2] for r in csvList]                # truncate newline chars
    readings = [re.split(r',',r,2) for r in readings]    # split str into two ',' delimiter
    return [(r[0],r[1]) for r in readings]               # convert list of lists [[][]] to list of tuples [()()]


def removeEmptyReadings(readings):
    """
    removes all readings which have a non digit watt value

    >>> r = [('2012-01-01T00:00:00','84'),('2013-08-01T01:01:01','[]')]
    >>> removeEmptyReadings(r)
    [('2012-01-01T00:00:00', '84')]

    """
    #readings = [r for r in readings if not r[1]=='[]']    # works in practice but not general enough
    readings = [r for r in readings if r[1].isdigit()]
    return readings


def convertToMPLDateTimes(readings):
    """
    converts string datetimes into datetimes suitable for matplotlib's date_plot function
    
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)

    >>> r = [('2012-01-01T00:00:00','84')]
    >>> convertToMPLDateTimes(r)
    [(734503.0, '84')]
    """
    # Alternative:
    # readings = [(dParser.parse(r[0]),r[1]) for r in readings]      # str to datetime objs
    # readings = [(mplDates.date2num(r[0]),r[1]) for r in readings]  # conv datetime to mpl time

    mplDateParser = mpl_strpdate2num(DATETIMEFORMAT)      # strpdate2num seems undocumented except in src code
    readings = [(mplDateParser(r[0]),r[1]) for r in readings]
    return readings


def convertToMPLDateTimes2(readings):
    """
    Converts repr of time: str -> datetime objs -> matplotlib times
    
    Alternative for first function as strpdate2num seems undocumented except in source code (is it deprecated?)
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)

    >>> r = [('2012-01-01T00:00:00','84')]
    >>> convertToMPLDateTimes2(r)
    [(734503.0, '84')]
    """
    readings = [(dt.datetime.strptime(r[0],DATETIMEFORMAT),r[1]) for r in readings]
    readings = zeroIndexTimesAxis(readings)                                 # zero index the time values
    return [(mpl_date2num(r[0]),r[1]) for r in readings]   # convert to mpl dates (floats)



def time(readings):
    """
    returns list of time values from first column of list of lists input

    >>> a = [['12-08-12',345],['12-08-13',123]]
    >>> time(a)
    ['12-08-12', '12-08-13']
    """
    return [time[:1][0] for time in readings]


def zeroIndexTimesAxis(readings):
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
    delta = d1 - d0
    return [[time[0] - delta, time[1]] for time in readings]


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


import doctest
doctest.testmod()
