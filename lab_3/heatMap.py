import pandas as pd
import utility as util
from datetime import datetime
import numpy as np
import seaborn as sbn
    
    
def generate_linklab_heatmap(start_datetime, end_datetime, fields, export_filepath):
    df = pd.read_csv('book_with_grids.csv')  # read in all of the data
    x = 0 # sets int
    y = 0
    n = 0
    numDataPoints = list() # makes a list to append the number of data points to
    while n < 200:
        sensors = list(df[(df['grid'] == n)]['device_id']) # gets all of the device ids for the sensors in that grid
        ldf = util.get_lfdf(fields, start_datetime, end_datetime, sensors) # gets all of the data for the specified variables
        numDataPoints[x, y] # appends the list with the number of data points retrieved
        if y == 19:
            y = 0
            x += 1
        else:
            y += 1
        n = 10*(2*y) + x # iterates through the loop

    dataLabeledBins = pd.cut(numDataPoints, 6, True, [1, 2, 3, 4, 5, 6]) # makes 6 bins of the data
    # returns an array of the same length as numDataPoints, except every data point is just the bin label
