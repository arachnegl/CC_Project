# from:
# http://stackoverflow.com/questions/7578689/median-code-explanation

def average(list_vals):
    """
    returns average of list of ints using built-in functions
    
    >>> print average([20,30,70])
    40

    """
    return sum(list_vals)/len(list_vals)


def median(list_vals):
    """
    returns the median value of list of ints. Chooses even index if list is even.

    >>> print median([6,5,4,3,2,1])
    3


    """
    
    sorted_list = sorted(list_vals)
    median_index = len(sorted_list) / 2
    return list_vals[median_index]


import doctest
doctest.testmod() # autovalidates embedded tests in docstrings
