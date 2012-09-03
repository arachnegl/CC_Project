"""
Various tools to synthesise days

"""

import datetime as dt
import matplotlib.dates as mdates


def dayRange():
    start = dt.datetime(2012,01,01,0,0,0)  # take minum time as arbitrary beg
    for n in range((60*60*24)/6):
        yield start + dt.timedelta(seconds = 6*n)


def getMPLDatesDayRange(interval):
    start = dt.datetime(2012,01,01,0,0,0)
    end = start + dt.timedelta(days=1)
    return mdates.drange(start,end,dt.timedelta(seconds=6))



