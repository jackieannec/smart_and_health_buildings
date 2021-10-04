df = pd.read_csv('book_with_grids.csv')  # read in all of the data
x = 0  # sets int
y = 0
n = 0
s= datetime(2021,1,1) # start datetime
e= datetime(2021,9,20) # end datetime
numDataPoints = [[0 for i in range(20)] for j in range(10)] # makes a list to append the number of data points to
fields = set(df['fields'])
fields2 = set()
for each in fields:
    alist = each.split(',')
    for abc in alist:
        fields2.add(abc)
fields = fields2
while n < 200:
    sensors = list(df[(df['grid'] == n)]['device_id'])  # gets all of the device ids for the sensors in that grid
    sums = 0
    for sense in sensors:
        for each in fields:
            print(fields)
            ldf = util.get_lfdf(each, s, e, sense) # gets all of the data for the specified variables
            if ldf is None:
                continue
            else:
                sums += len(ldf)
    numDataPoints[x][y] = sums  # appends the list with the number of data points retrieved
    if y == 19:
        print('two')
        y = 0
        x += 1
    else:
        print('one')
        y += 1
    print('------------------------------------------------------------------------------')
    n += 1
print(numDataPoints)
