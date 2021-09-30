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
        fields = list(set(df[df['grid'] == n]['fields'].values[0].split(',')))
        z = 0
        sums = 0
        while z < len(fields):
            ldf = util.get_lfdf(fields[z], start_datetime, end_datetime, sensors) # gets all of the data for the specified variables
            sums += len(ldf)
            z += 1
        numDataPoints[y][x] = sums  # appends the list with the number of data points retrieved
        if y == 19:
            y = 0
            x += 1
        else:
            y += 1
        n = 10 * (2 * y) + x  # iterates through the loop

    dataLabeledBins = pd.cut(numDataPoints, 6, True, [1, 2, 3, 4, 5, 6])  # makes 6 bins of the data
