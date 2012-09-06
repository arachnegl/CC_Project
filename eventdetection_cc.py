


def applianceEventDetection(start,step,reading):
    """

    >>> l = [(0,30),(0,30),(0,80),(0,80),(0,40),(0,30)]
    >>> applianceEventDetection(0,30,l)
    (1, 5)

    """
    i = start
    beg = 0
    end = 0
    begFound = False
 #   import pdb; pdb.set_trace()
    for el in reading:
        jump = abs(reading[i+1][1] - reading[i][1])
        if jump > step and not begFound:
            beg = i
            begFound = True
            i = i + 1
            continue
        if jump > step and begFound:
            end = i + 2                 # add a little padding
            break
        i = i + 1
    return (beg,end)


import doctest
doctest.testmod()
