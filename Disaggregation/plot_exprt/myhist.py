

def fillHistValues(valSrc):
    """

    >>> fillHistValues([['-','1'],['-','2'], ['-','2'],['-','2']])
    [0, 1, 3, 0]

    # test case of unequal arrays + raise exception?
    """
    # the returned array will have to be changed into a key value type table at some point.
    histogram = [0 for i in range(len(valSrc))]   # generate array of 0s

 #   import pdb; pdb.set_trace()
    for val in valSrc:
        index = int(val[1])  # first value is ignored, second value determines index of output array
        histogram[index] = histogram[index] + 1
    return histogram


import doctest
doctest.testmod()
