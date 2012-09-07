"""
Put all expr here

"""

import io_cc as io
import plt_cc as pc
import logictosignals_cc as ls
import appldata_cc as ad
import timeutils_cc as tu
import abdparser_cc as abp
import eventdetection_cc as ed

import numpy as np
import matplotlib.pyplot as plt


#  Appliance analysis graph    ( 1 step)
ovenAnalysis = pc.getAnalysisTimeWattFigure(ad.oven,'oven analysis')

# smoothing eg graph   (1 step)
grSmth = pc.getSmoothFigure(ad.grill)

# Convolution Graph  (3 steps)
rs = ad.appReadings   # io.getReadingsFromFile('appliance_data_clean.csv')
gr_cnv = ls.getConvolve(ad.grill,rs)
gr_cnv_fig = pc.getConvolveFigure(gr_cnv,rs)

# Hist graph   ( 1 step)
appldatahist = pc.getHistFig(ad.appReadings,binsN=1000,name='Appliance Readings')

# Abduction
# get predicates:
fctList = abp.getFactsFromFile('day_night_worker.pl')  # rtrns ['lunch(p)'.'fluctuations(greg).']

# test predicates:

