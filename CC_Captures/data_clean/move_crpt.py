#!/usr/bin/python

"""
1)  gets list of files
2)  strips list to capture files
-a   if stripped list is empty exit
3)  sorts list
-a   saves last list elmnt
4)  moves each element in list by iterating if not last (youngest) file
"""

import sys, os, subprocess, re


def isCCFileName(fName):
    """ 
    predicate: True if fName is of format 'cc_timestamp.csv' 

    >>> isCCFileName('cc_2012-07-28T00:28:02.csv')
    True
    
    >>> isCCFileName('Xcc_2012-07-28T12:12:12.csv')
    False

    >>> isCCFileName('awef')
    False
    """
    found = re.findall(r'cc_[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.csv',fName)
    if len(fName) == 26 and len(found) == 1:       
        # IF  test 1: string not larger than expected 
        # AND test 2: one (and only one) regexpr match found
        return True
    else:
        return False

def getListOfCCFiles():
    """
    returns list of capture files. If none returns empty list.

    How do I test this? Unit testing?
    """
    dirListing = os.listdir('.')
    dirStripped = [fName for fName in dirListing if isCCFileName(fName)]    
    dirSorted = sorted(dirStripped)
    return dirSorted

    # last_entry = dirSorted[len(dirSorted)-1]
    # gen expr more optimal than creating new list with list comprehension:
    # for n in (fName for fName in dirSorted if fName != last_entry):
    #    print(n)

"""
# No longer needed as will never run as script again.

def move_files(destPath):
    listToMove = getListOfCCFiles()[:-1]  # truncate most recent (prob in use)
    for fname in listToMove:
        subprocess.call("mv" + " " + fname + " " + destPath ,shell=True) 


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: this script needs a path argument'
        sys.exit(-1)
    dPath = args[0]
    move_files(dPath)  # dangerous to uncomment test first!

if __name__ == '__main__':
    main()
"""

import doctest
doctest.testmod()
