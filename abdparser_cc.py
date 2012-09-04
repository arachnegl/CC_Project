"""
Abductive Logic File Parser

Typical usage:
    listOfFacts = getFactsFromFile('abductive.pl')

"""

import re

PREDICATE_RE = r"[a-z]+\([a-z]+\)\.$"

def getLines(aFile):
    """
    Returns list of file contents.
    """
    with open(aFile) as f:
        contents = f.readlines()
    return contents

def getPredicatesFrom(aList):
    """
    returns all valid predicates contained in a list of strings with newlines

    >>> aList = ['one string\\n','one other string\\n','predicate(string).\\n']
    >>> getPredicatesFrom(aList)
    ['predicate(string).']

    NB  that there are escape sequences in the aList example. 
        This is for docstring purposes and
        Not part of the code itself
    """
    return [l[:-1] for l in aList if containsFact(l)]

def containsFact(aStr):
    """
    returns true if match

    >>> True == containsFact('awef(awef).')
    True

    """
    if re.match(PREDICATE_RE,aStr):    # NB re.match only rtrns if at beg of str (so no need for ^)
        return True
    else :
        return False


def getFactsFromFile(aFile):
    """
    Wrapper function for this module
    """
    c = getLines(aFile)
    c = getPredicatesFrom(c)
    return c


import doctest
doctest.testmod()  # auto validation of embedded docstrings
