import pandas as pd
import utility as util
from datetime import datetime
import numpy as np
import seaborn as sbn
    
    
def generate_linklab_heatmap(start_datetime, end_datetime, fields, export_filepath):
    df = pd.read_csv('book_with_grids.csv')  # read in all of the data
    n = 0
    numDataPoints = list()
    while n < 200:
        sensors = list(df[(df['grid'] == n)]['device_id'])
        ldf = util.get_lfdf(fields, start_datetime, end_datetime, sensors)
        numDataPoints.append(len(ldf))
        n += 1

    maxData = max(numDataPoints)
    for i in range(len(numDataPoints)):
        if numDataPoints[i] != 0:
            temp = numDataPoints[i]/maxData
            numDataPoints[i] = temp

    bins = pd.Series(pd.qcut(numDataPoints, 6)).value_counts()
