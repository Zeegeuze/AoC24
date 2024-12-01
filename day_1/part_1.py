import pandas as pd

def day1(filename):
    data = pd.read_csv(filename, names=['col1', 'col2'], sep='   ')
    left = data['col1'].sort_values().reset_index(drop=True)
    right = data['col2'].sort_values().reset_index(drop=True)

    sum = (right - left).abs().sum()

    return sum

print(day1("day_1/input_1.txt"))
