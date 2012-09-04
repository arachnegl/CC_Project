"""
File contains a variety of statistical analysis functions to aid analysis and decision making



# future helper function for fillHistValues?

    # Slice the array to contain only recorded values
    minWatt = int(min([val[1] for val in valSrc]))
    maxWatt = int(max([val[1] for val in valSrc]))

    histogram = histogram[minWatt:maxWatt]
"""

def getHist(valSrc):
    """
    Returns list of ints. Index of list are watt values. The values at each index are the total count of readings corresponding to that watt value.

    >>> getHist([1,2,2,2])
    [0, 1, 3]

    # test case of unequal arrays + raise exception?
    """
    # generate zeroed array of appropriate size:
    length = max(valSrc) + 1
    histogram = [0 for i in range(length)]

    for val in valSrc:
        index = int(val) 
        histogram[index] = histogram[index] + 1

    return histogram



def removePhantomEnergy(valList):
    """
    Returns 
    """
    histValList = getHist(valList)
    minVal = histValList.index(max(histValList)) + 5

    normalise = [x-minVal for x in valList]
    normalise = [0 if x<0 else x for x in normalise]

    return normalise


def cleanSignal(watts):
    """
    Returns a smoothened and normalised signal.
    """
    watts = smooth(watts)
    watts = removePhantomEnergy(watts)

    return watts


def fillHistValues(valSrc):
    """
    returns a list of two valued lists containing a count for each energy value read

    >>> fillHistValues([['-','1'],['-','2'], ['-','2'],['-','2']])
    [[0, 0], [1, 1], [2, 3], [3, 0]]

    # test case of unequal arrays + raise exception?
    """
    # the returned array will have to be changed into a key value type table at some point.
    histogram = [[i,0] for i in range(len(valSrc))] # generate array of (wattVal,0)s

    for val in valSrc:
        index = int(val[1])  # first value is ignored, second value determines index of output array
        histogram[index][1] = histogram[index][1] + 1

    return histogram


def fillHistValues2(valSrc):
    """
    returns a list of two valued lists containing a count for each energy value read

    >>> fillHistValues2([1,2,2,2])
    [0, 1, 3]

    # test case of unequal arrays + raise exception?
    """
    # the returned array will have to be changed into a key value type table at some point.
    histogram = [0 for i in range(max(valSrc)+1)] # generate na array of zeros

    for val in valSrc:
        index = val  # first value is ignored, second value determines index of output array
        histogram[val] = histogram[val] + 1

    return histogram


def getWattCount(valSrc):
    """

    >> getWattCount([['-','1'],['-','2'], ['-','2'],['-','2']])
    {'1': 1, '2': 3}
    """
    pass
    

def average(intList):
    """
    returns average of list of ints using built-in functions
    
    >>> print average([20,30,70])
    40
    """
    return sum(intList)/len(intList)


def median(intList):
    """
    returns the median value of list of ints. Chooses even index if list is even.

    >>> print median([6,5,4,3,2,1])
    3
    """
    
    sortedList = sorted(intList)
    indexOfMedian = len(sortedList) / 2
    return intList[indexOfMedian]


import doctest
doctest.testmod() # autovalidates embedded tests in docstrings
