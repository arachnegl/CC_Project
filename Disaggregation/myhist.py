


def fillHistValues(valSrc):
    """
    returns a list of two valued lists containing a count for each energy value read

    >>> fillHistValues([['-','1'],['-','2'], ['-','2'],['-','2']])
    [[0, 0], [1, 1], [2, 3], [3, 0]]

    # test case of unequal arrays + raise exception?
    """
    # the returned array will have to be changed into a key value type table at some point.
    histogram = [[i,0] for i in range(len(valSrc))] # generate array of (wattVal,0)s

 #   import pdb; pdb.set_trace()
    for val in valSrc:
        index = int(val[1])  # first value is ignored, second value determines index of output array
        histogram[index][1] = histogram[index][1] + 1

    # Slice the array to contain only recorded values
#    minWatt = int(min([val[1] for val in valSrc]))
#    maxWatt = int(max([val[1] for val in valSrc]))

#    histogram = histogram[minWatt:maxWatt]
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

    # Slice the array to contain only recorded values
#    minWatt = int(min([val[1] for val in valSrc]))
#    maxWatt = int(max([val[1] for val in valSrc]))

#    histogram = histogram[minWatt:maxWatt]
    return histogram

def getWattCount(valSrc):
    """

    >> getWattCount([['-','1'],['-','2'], ['-','2'],['-','2']])
    {'1': 1, '2': 3}
    """
    pass
    



import doctest
doctest.testmod()
