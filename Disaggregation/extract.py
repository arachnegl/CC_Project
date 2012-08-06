import csv, sys

def extractValues(csvFile):
    """
    Returns a list of two value lists stripping entries with no numeric values. (In practice '[]')

    Raises:
	IOError: if csvFile not found
        csv.Error: if error in csvFile
    """ 
    readings = []
    lRead = 0
    nVals = 0

    with open(csvFile, 'r') as f: 
        reader = csv.reader(f)
        try:
            for line in reader:
                lRead += 1
                if line[1].isdigit():
                    nVals += 1
                    readings.append(line)
                else:   # value is '[]' so no reading, ignore
                    continue
        except csv.Error, e:
            sys.exit('file %s, line %d,: $s' % (filename, reader.line_num, e))
        else:
            print("Finished extraction. Lines read: %s Actual Readings: %s" 
                     %(lRead,nVals)) 
# probably to be added to unittests:
    if [x for x in readings if not x[1].isdigit()] == [] and len(readings) == nVals:
        return readings
    else:
        return -1


def time(readings):
    """
    returns list of time values from first column of list of lists input

    >>> a = [['12-08-12',345],['12-08-13',123]]
    >>> time(a)
    ['12-08-12', '12-08-13']
    """
    return [time[:1][0] for time in readings]

def watts(readings):
    """
    returns list of watt values from second column of list of lists input

    >>> a = [['12-08-12',345],['12-08-13',123]]
    >>> watts(a)
    [345, 123]
    """
    return [watts[1:][0] for watts in readings]


import doctest
doctest.testmod()
