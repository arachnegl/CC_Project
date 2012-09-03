

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

import doctest
doctest.testmod()

"""
if __name__=='__main__':
    smooth_demo()
"""
