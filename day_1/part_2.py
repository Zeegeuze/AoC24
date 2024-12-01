import pandas as pd

def day1(filename):
    data = pd.read_csv(filename, names=['col1', 'col2'], sep='   ')

    sum = 0

    for index, row in data.iterrows():
        sum += (row[0] * data['col2'].value_counts().get(row[0], 0))

    return sum

print(day1("day_1/input.txt"))
