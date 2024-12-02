def day_2(filename):
    sum = 0
    with open(filename, "r") as f:
        rows = f.read().split("\n")

    for row in rows:
        if row != '':
            splitted = list(map(int, row.split(" ")))

            # Test if all are ascending or descending
            if splitted == sorted(splitted) or splitted == sorted(splitted, reverse=True):

                # Test if difference between the numbers is from 1 to 3
                diffs = []
                for i in range(len(splitted)-1):
                    diffs.append(abs(splitted[i+1] - splitted[i]))
                res = [i for i in diffs if i not in [1, 2, 3]]
                if res == []:
                    sum += 1

    return sum


print(day_2("day_2/input.txt"))
