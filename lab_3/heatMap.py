import pandas as pd
import utility as util
from datetime import datetime
import numpy as np
import seaborn as sbn
import matplotlib as mpl

def generate_linklab_heatmap(start_datetime, end_datetime, fields, export_filepath):
    df = pd.read_csv('book_with_grids.csv')  # read in all of the data
    x = 0  # sets int
    y = 0
    n = 0
    numDataPoints = [[0 for i in range(20)] for j in range(10)]# makes a list to append the number of data points to
    while n < 200:
        sensors = list(df[(df['grid'] == n)]['device_id'])  # gets all of the device ids for the sensors in that grid
        sums = 0
        for sense in sensors:
            for each in fields:
                ldf = util.get_lfdf(each, s, e, sense)  # gets all of the data for the specified variables
                print(ldf)
                if ldf is None:
                    continue
                else:
                    sums += len(ldf)
        numDataPoints[x][y] = sums  # appends the list with the number of data points retrieved
        if y == 19:
            y = 0
            x += 1
        else:
            y += 1
        n += 1 # iterates through the loop

    map_img = mpl.image.imread('./img/lll_grid.png')
    hmax = sbn.heatmap(numDataPoints, alpha=0.5, zorder=2)
    hmax.imshow(map_img, aspect=hmax.get_aspect(), extent=hmax.get_xlim() + hmax.get_ylim(), zorder=1) #put the map under the heatmap
    mpl.pyplot.show()
