"""
This module defines various input functions for parsing and loading readings from cc files

It also includes some functions for cleaning the data and extracting watts and times arrays

you probably want to use getReadingsFromFile(yourFile).

"""

import numpy as np
import re

import timeutils_cc as cct

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




def clean(readings):
    """
    removes all non digit watt values and converts to int

    >>> r = [('2012-01-01T00:00:00','84'),('2013-08-01T01:01:01','[]')]
    >>> removeNonDigitReadings(r)
    [('2012-01-01T00:00:00', 84)]

    """
    #readings = [r for r in readings if not r[1]=='[]']    # works in practice but not general enough
    readings = [(r[0],int(r[1])) for r in readings if r[1].isdigit()]
    return readings


def removeEmptyReadingsFromFile(aFile):
    """
    Strips empty readings marked as watt readings of '[]' from a current cost data file
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


def getReadingsFromFile(ccFile):
    """
    Wrapper around functions above 

    """
    readings = extractValuesFromCCFile(ccFile)
    readings = clean(readings)
    readings = cct.convertStrDateTimesToMPLDateTimes(readings)
    return readings


import doctest
doctest.testmod()
