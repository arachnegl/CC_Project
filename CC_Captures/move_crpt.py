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


def isCCFileName(s):
    """ 
    predicate: True if s contains timestamp and cc 

    >>> isCCFileName('2012-07-28T00:28:02_cc.csv')
    True

    >>> isCCFileName('awef')
    False
    """
    result = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}_cc.csv',s)
    if result == []:       # test 1: if empty list regexpr didn't return match
        return False
    result = result[0]
    if len(result) != 26:  # test 2: string not larger than expected
        return False
    else:
        return True

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

import doctest
doctest.testmod()
