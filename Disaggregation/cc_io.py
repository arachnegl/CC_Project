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



readings = np.loadtxt('appliance_study_data.csv',
                      delimiter=',',unpack=False,
                      dtype={'names':('time','watt'),
                             'formats':('S19','S4')}
                      )

"""
# Alternatively: (dflt dtype is float)
time,watts = np.loadtxt(fName,unpack=True,
                        converters={0:mpl.dates.strpdate2num('%Y-%m-%dT%H:%M:%S')},
                        delimiter=',')

"""



# import the smooting algos at some point


readings = [r for r in readings if not r[1]=='[]']    # strip out empty reads
readings = [(dParser.parse(r[0]),r[1]) for r in readings]  # str to datetime objs
readings = [(mplDates.date2num(r[0]),r[1]) for r in readings]  # conv datetime to mpl time
# alt:
#mplDateParser = mplDates.strpdate2num('%Y-%m-%dT%H:%M:%S') # if you know the str format
#readings = [(mplDateParser(r[0]),r[1] for r in readings]

# print(readings[0]) # rtrns  (734724.4361805556, '84')

times = [r[0] for r in readings]
watts = [r[1] for r in readings]


def getReadings(fileName):
    """
    returns file contents as list of lines 
    """
    with open(fileName,'r') as f:
        return [r for r in f.readlines()]

def csvToList(csvList):
    """
    ['2012-09-07T12:01:02,211'] -> [['2012-09-07T12:01:02','211']]

    csv parser better than below - but wanted to experiment)
    """
    readings = [r[0:-2] for r in csvList]              # truncate newline chars
    return [re.split(r',',r,2) for r in readings]      # split str into two ',' delimiter



def convertTimes(readings):
    """
    Converts repr of time: str -> datetime objs -> matplotlib times
    
    (Matplotlib represents time as float since 0001-01-01 00:00:00 UTC)
    """
    readings = [[dt.datetime.strptime(r[0],"%Y-%m-%dT%H:%M:%S"),r[1]] for r in readings]
    readings = zeroIndexTimesAxis(readings)                                 # zero index the time values
    return [[mpl.dates.date2num(r[0]),r[1]] for r in readings]   # convert to mpl dates (floats)



def time(readings):
    """
    returns list of time values from first column of list of lists input

    >>> a = [['12-08-12',345],['12-08-13',123]]
    >>> time(a)
    ['12-08-12', '12-08-13']
    """
    return [time[:1][0] for time in readings]


def zeroIndexTimesAxis(readings):
    """
    Zero indexes a list of times. 
    Purpose: graph starts from time 0 instead of when readings started.  
    (A better implementation would perhaps use min UTC but had probs with this.)

    Function assumes and only makes sense if readings take place within a single day
    """
    time0 = readings[0][0]                                              # get first reading
    d0 = time0.strftime(format="%Y-%m-%dT%H:%M:%S")[:10] + "T00:00:00"  # set d0 to beg of day
    d0 = dt.datetime.strptime(d0,"%Y-%m-%dT%H:%M:%S")
    d1 = time0
    delta = d1 - d0
    return [[time[0] - delta, time[1]] for time in readings]


def getTimes(readings):
    """
    returns first column in list with 'two columns'

    eg: [[a,b]] -> [a]

    """
    return [r[0] for r in readings]

def getWatts(readings):
    """
    returns second column in list with 'two columns'

    eg: [[a,b]] -> [b]

    """
    return [r[1] for r in readings]


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
