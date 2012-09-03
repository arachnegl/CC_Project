"""
Appliance data

suggested usage:
    import appData as ad

"""

import io_cc as io   # for getTimes and getWatts


listOfApp = ['grill','oven','microwave',
       'tv','washingMachine','dishWasher',
       'toaster']

appReadings = io.getReadingsFromFile('appliance_data_clean.csv')


grill = appReadings[335:388]
oven = appReadings[61:172]
microwave = appReadings[652:671]
tv = appReadings[723:841]
washingMachine = appReadings[1092:1710]
dishWasher = appReadings[1818:2097]
toaster = appReadings[9:29]
