"""
Code to make all cc_files coherent: 
strip all non readings and split them up into day files

You probably only want to use createDayCCFiles

"""

import os, re, csv
import datetime as dt

# Variables that determine filenames:
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'
RAW_FILE_ENDING = '_cc.csv'
NEW_FILE_ENDING = 'clean_cc.csv'


def createDayCCFiles(srcFolder,destFolder):
    """
    Main Function use it
    """
    ccFiles = getCCFilesFromDir(srcFolder)
    readings = getAllReadings(ccFiles)
    os.chdir(destFolder)
    writeReadingsToDayFiles(readings)


def isRawCCFileName(fName):
    """ 
    predicate: True if fName arg is of format 'timestamp_cc.csv' 

    used as helper function to getCCFilesFromDir

    >>> isRawCCFileName('2012-07-28T00:28:02_cc.csv')
    True
    
    >>> isRawCCFileName('Xcc_2012-07-28T12:12:12.csv')
    False

    >>> isRawCCFileName('awef')
    False
    """
    regExpr = r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}_cc.csv' 
	# could restrict re further according to valid date values
    found = re.findall(regExpr,fName)
    if len(fName) == 26 and len(found) == 1:       
        # IF  test 1: string not larger than expected 
        # AND test 2: one (and only one) regexpr match found
        return True
    else:
        return False

def getCCFilesFromDir(pathName):
    """
    returns a sorted list of cc files from directory given as argument.

    The timestamp in a ccfile name ensures that the list of files can be sorted.
    """
    files = os.listdir(pathName)
    files = [f for f in files if isRawCCFileName(f)]
    files = [pathName + f for f in files]          # add the path
    files = sorted(files)
    return files


def getFilesByDateStamp(dtStmp,fileList):
    """
    returns a list of all files in cwd with datestamp in file name equal to argument

    >>> files = ['CC_2012-07-28T00:26:34_cc.csv','CC_2013-02-27T05:45:12_cc.csv','CC_2012-07-27T00:26:34_cc.csv','CC_2012-07-28T23:52:21_cc.csv']
    >>> getFilesByDateStamp('2012-07-28',files)
    ['CC_2012-07-28T00:26:34_cc.csv', 'CC_2012-07-28T23:52:21_cc.csv']
    """
    files = []
    for fileName in fileList:
        fileDate = fileName[3:13]
        if fileDate == dtStmp:
            files.append(fileName)
    return files


def isDateChanged(timeStr):
    """
    returns boolean. Confirms if midnight has passed.

    helper function for getAllReadings
    """
    return re.findall(r'00:00:[0-9][0-9]',timeStr)


def getAllReadings(fileList):
    """
    returns a list of all readings found
    """
    dtype = [] # datatype will be populated with all [timestamp,watt] pairs
    # create super list of all the readings:
    for fName in fileList:
        dtName = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",fName)[0]
        currDate = dt.datetime.strptime(dtName,DATE_FORMAT) # curr date is file name
    
        with open(fName,'r') as f:
            nextDay = False   # date changed only once
            reader = csv.reader(f)
            for line in reader:      # reader rtrns ['time','watt'] per row

                if isDateChanged(line[0][:8]) and not nextDay:
                    currDate = currDate + dt.timedelta(days=1)  # increment currDate
                    nextDay = True

                # this clause deals with old file recordings that didn't include a full datetime str
                if len(line[0]) == 8 :  # only apply on lines that don't have full datetime str
                    line[0] = currDate.isoformat()[:10] + 'T' + line[0]

                if line[1].isdigit():
                    dtype.append(line)
    return dtype




def writeReadingsToDayFiles(readings):
    """
    writes all readings to disk in one day files

    """
    # create new files for each value in date change
    locDateChngs = getListOfDateChanges(readings)
    locDateChngs.append(len(readings))   # to capture last reading
    
    for nmbr in range(len(locDateChngs) - 1):
        daySlice = readings[locDateChngs[nmbr]:locDateChngs[nmbr+1]]  # slice corresponding to day
        writeToDisk(daySlice)


def getListOfDateChanges(readings):
    """
    returns a list of all the indexes where a date change occurs
    
    (helper function for writeReadingsToDayFiles)
    """
    # get list of all the date changes:
    dateChngs = []
    for i in range(len(readings)):
        if not readings[i-1][0][:10] == readings[i][0][:10]:      # first is 0 as last diff from 0
            dateChngs.append(i)
    return dateChngs


def writeToDisk(readings):
    """
    writes a list to disk as csv file
    
    (helper function to writeReadingsToDayFiles)
    """  
    # new fileNames is timestamp of 1st val + globally defined ending:
    fName = readings[0][0][:10] + NEW_FILE_ENDING

    with open(fName,'w') as f:
        writer = csv.writer(f)
        writer.writerows(readings)


def getFirstDate(dtStrFileList):
    """
    returns datetime obj that represents first date found in a list of DATETIME_FORMAT strings

    """
    dtStrFileList = sorted(dtStrFileList)
    first_dtStr = dtStrFileList[0]
    fDate = dt.datetime.strptime(first_dtStr,DATETIME_FORMAT + RAW_FILE_ENDING)
    return fDate

def getLastDate(dtStrFileList):
    """
    returns datetime obj that represents last date found in a list of DATETIME_FORMAT strings

    """
    dtStrFileList = sorted(dtStrFileList)
    last_dtStr = dtStrFileList[-1]
    lDate = dt.datetime.strptime(last_dtStr,DATETIME_FORMAT + RAW_FILE_ENDING)
    return lastDate


import doctest
doctest.testmod()
