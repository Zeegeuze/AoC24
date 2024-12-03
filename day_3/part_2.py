import re

def day_3(filename):
    with open(filename, "r") as f:
        corrupted = f.read()

    dos = corrupted.split('do()')

    muls = []
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    for do in dos:
        active_part = do.split("don't()")[0]
        muls = muls + re.findall(pattern, active_part)

    sum = 0

    for i in muls:
        parts = i.split(",")
        sum += (int(parts[0][4:]) * int(parts[1][:-1]))

    return sum

print(day_3("day_3/input.txt"))
