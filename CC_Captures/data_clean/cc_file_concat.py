import os, re, csv

files = os.listdir('.')
# discard all but .csv files:
files = [f for f in files if re.findall(r".*.csv",f)]
files = sorted(files) # timestamp in title ensures sorted in order




dtype = [] # this will be populated with all [timestamp,watt] pairs

for fName in files:
    fDate = f[:10]  # the date is the first 8 chars of filename
    print(fDate)
    with open(fName,'r') as openF:
        reader = csv.reader(openF)
        for line in reader:
            line[0] = fDate + 'T' + line[0]
            dtype.append(line)
