import re

def day_3(filename):
    with open(filename, "r") as f:
        corrupted = f.read()

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    muls = re.findall(pattern, corrupted)

    sum = 0

    for i in muls:
        parts = i.split(",")
        sum += (int(parts[0][4:]) * int(parts[1][:-1]))

    return sum


print(day_3("day_3/input.txt"))
