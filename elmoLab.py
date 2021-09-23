import pandas as pd
df = pd.read_csv('Lab2Data')
# print(df)
num_students = 18
assignComplete = len(df['username'])

# question 2
twoAns = num_students - assignComplete
print(twoAns)


# question 3
elmoLike = df[df['sesame'].isin(['elmo'])]
threeAns = len(elmoLike)
print(threeAns)

# question 4
cookieNight = df.loc[df['sesame'].isin(['cookie']) & df['sleep'].isin(['night owl'])]
fourAns = len(cookieNight)
print(fourAns)

# question 5
elmoRockMorning = df.loc[(df['sesame'] != 'elmo') & (df['rps'] != 'rock') & (df['sleep'] == 'morning bird')]
fiveAns = len(elmoRockMorning)
print(fiveAns)

