import os, re, csv
import datetime as dt

files = os.listdir('.')
files = [f for f in files if re.findall(r'2012.*cc.csv',f)] # only these project files
files = sorted(files) # timestamp in title ensures sorted in order


dtype = [] # this will be populated with all [timestamp,watt] pairs

firstDate = dt.datetime.strptime(files[0],'%Y-%m-%dT%H:%M:%S_cc.csv')
lastDate = dt.datetime.strptime(files[-1],'%Y-%m-%dT%H:%M:%S_cc.csv')
oneDay = dt.timedelta(days=1)

for fName in files:
    currDate = dt.datetime.strptime(fName[:18],'%Y-%m-%dT%H:%M:%S') # curr date is file name
    
    with open(fName,'r') as openF:
        nextDay = False   # date changed only once
        reader = csv.reader(openF)
        for line in reader:      # reader rtrns ['time','watt'] per row
            if re.findall(r'00:00:[0-9][0-9]',line[0][:8]) and not nextDay:
                currDate = currDate + oneDay
                nextDay = True
            
            line[0] = currDate.isoformat()[:10] + 'T' + line[0]
            if line[1].isdigit():
                dtype.append(line)


indexDateChngs = []

for i in range(len(dtype)):
    if not dtype[i-1][0][:10] == dtype[i][0][:10]: # first is 0 as last diff from 0
        indexDateChngs.append(i)


for nmbr in range(len(indexDateChngs) - 1):
    newList = dtype[indexDateChngs[nmbr]:indexDateChngs[nmbr+1]]
    with open(newList[0][0][:10] + 'new.csv','w') as wFile:
        writer = csv.writer(wFile)
        writer.writerows(newList)



"""
# this approach to date iteration was found on stackexchange. Its a far more elegant solution than my experiments.

# generator function
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for date in daterange(firstDate,lastDate+oneDay):
    nextDay = date + oneDay
        while date.isoformat()[:10] == and not nextDay

currDay = dt.datetime.strptime(reading[0][:10],'%Y-%m-%d')
newDay = currDay + oneDay

for reading in dtype:
    with open(currDay.isoformat() + 'new.csv','w') as dateFile:
        writer = csv.writer(dateFile)
        if currDay < newDay:
            writer.writerow(reading)
        else:
            currDay + oneDay
            newDay + oneDay    



# I tried an approach to create a table w rows: <date><[list,of,readings]>
 
""" 
