import pandas as pd
import utility as util
from datetime import datetime
import numpy as np
import seaborn as sbn

def generate_linklab_heatmap(start_datetime, end_datetime, fields, export_filepath):
    df = pd.read_csv('book_with_grids.csv')  # read in all of the data
    x = 0  # sets int
    y = 0
    n = 0
    numDataPoints = [[0 for i in range(20)] for j in range(10)]# makes a list to append the number of data points to
    while n < 200:
        sensors = list(df[(df['grid'] == n)]['device_id'])  # gets all of the device ids for the sensors in that grid
        fields = list(set(df[df['grid'] == n]['fields']))
        fields2 = set()
        for each in fields:
            alist = each.split(',')
            for abc in alist:
                fields2.add(abc)
        z = 0
        sum = 0
        for each in fields2:
            ldf = util.get_lfdf(each, s, e, sensors) # gets all of the data for the specified variables
            if ldf is None:
                sum += 0
            else:
                sum += len(ldf)
        numDataPoints[x][y] = sum  # appends the list with the number of data points retrieved
        if y == 19:
            y = 0
            x += 1
        else:
            y += 1
        n += 1 # iterates through the loop

    dataLabeledBins = pd.cut(numDataPoints, 6, True, [1, 2, 3, 4, 5, 6])
