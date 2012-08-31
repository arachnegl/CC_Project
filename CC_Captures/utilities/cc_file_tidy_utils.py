import os, re


def isNewCCFileName(fName):
    """ 
    predicate: True if fName is of format 'cc_timestamp.csv' 

    >>> isNewCCFileName('cc_2012-07-28T00:28:02.csv')
    True
    
    >>> isNewCCFileName('Xcc_2012-07-28T12:12:12.csv')
    False

    >>> isNewCCFileName('awef')
    False
    """
	# could restrict re further according to valid date values
    regExpr = r'cc_[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.csv'
    found = re.findall(regExpr,fName)
    if len(fName) == 26 and len(found) == 1:       
        # IF  test 1: string not larger than expected 
        # AND test 2: one (and only one) regexpr match found
        return True
    else:
        return False


def isOldCCFileName(fName):
    """ 
    predicate: True if fName is of format 'timestamp_cc.csv' 

    >>> isOldCCFileName('2012-07-28T00:28:02_cc.csv')
    True
    
    >>> isOldCCFileName('Xcc_2012-07-28T12:12:12.csv')
    False

    >>> isOldCCFileName('awef')
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


def getSetOfOldCCFiles(path = '.'):
    """
    returns set of files with old format name.
    If none found returns empty set.

    """
    s = set(os.listdir(path))
    s = {fName for fName in s if isOldCCFileName(fName)}   
    return s


def translateFileName(oldName):
    """
    translates old file names to new format.

    >>> translateFileName('2012-07-28T00:28:02_cc.csv')
    'CC_2012-07-28T00:28:02.csv'
    """
    timeStamp = oldName[:19]
    return "CC_" + timeStamp + ".csv"


def renameFiles(fileList):
    """
    reformats the names of a list of cc files

    """
    for oldFileName in fileList:
        newFileName = translateFileName(oldFileName)
        os.rename(oldFileName,newFileName)


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


import doctest
doctest.testmod()
