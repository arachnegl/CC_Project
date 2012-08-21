import os, re

files = os.listdir('.')
# discard all but .csv files:
files = [f for f in files if re.findall(r".*.csv",f)]
files = sorted(files) # timestamp in title ensures sorted in order

dtype = [] # this will be populated with all [timestamp,watt] pairs

for f in files:
    date = f[:10]  # the date is the first 8 chars of filename
    print(date)
    with open(f,'r') as currFile:
        for line in currFile:
            if line[0][:8] != '00:00:0':
                dtype.append([date + 'T'+ line[:8]]+[line[9:]])
