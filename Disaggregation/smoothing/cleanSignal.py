
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



def normalise(valList):
    """
    Returns 
    """
    histValList = getHist(valList)
    minVal = histValList.index(max(histValList)) + 5

    normalise = [x-minVal for x in valList]
    normalise = [0 if x<0 else x for x in normalise]

    return normalise


def smooth(valList):
    """
    Smoothes the values
    """
    # placeholder
    pass


def cleanSignal(valList):
    """
    Returns a smoothened and normalised signal.
    """
    smoothed = smooth(valList)
    normalised = normalise(valList)

    return normalised

import doctest
doctest.testmod()
