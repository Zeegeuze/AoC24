# Still missing some edge casesn hence not correct...

def check_full_equal(list):
    list_without_last = list[0:len(list)-1]
    list_without_first = list[1:len(list)]

    if list == sorted(list) or list == sorted(list, reverse=True):
        return "list"
    elif list_without_last == sorted(list_without_last) or list_without_last == sorted(list_without_last, reverse=True):
        return "list_without_last"
    elif list_without_first == sorted(list_without_first) or list_without_first == sorted(list_without_first, reverse=True):
        return "list_without_first"
    else:
        return False

def check_equal_plus2(list):
    bigger = []
    for i in range(len(list)-2):
        bigger.append(list[i] > list[i+2])
    return len(set(bigger)) == 1

def check_no_differences(list):
    diffs = []
    for i in range(len(list)-2):
        diffs.append(abs(list[i+2] - list[i]))
    res = [i for i in diffs if i not in [1, 2, 3]]
    return len(res) == 1


def day_2(filename):
    sum = 0
    with open(filename, "r") as f:
        rows = f.read().split("\n")

    for row in rows:
        print(row)
        if row != '':
            splitted = list(map(int, row.split(" ")))

            # Test if all are ascending or descending
            checked_equal = check_full_equal(splitted)
            if checked_equal == 'list':
                checked_equal = splitted
                # Test if difference between the numbers is from 1 to 3
                diffs = []
                for i in range(len(checked_equal)-1):
                    diffs.append(abs(checked_equal[i+1] - checked_equal[i]))
                print(diffs)
                res = [i for i in diffs if i not in [1, 2, 3]]
                if len(res) < 2:
                    print('add 1')
                    sum += 1

            elif checked_equal == 'list_without_last':
                checked_equal = list[0:len(splitted)-1]

                diffs = []
                checked_equal = splitted[0:len(splitted)-1]
                for i in range(len(checked_equal)-1):
                    diffs.append(abs(checked_equal[i+1] - checked_equal[i]))
                res = [i for i in diffs if i not in [1, 2, 3]]
                if res == []:
                    print('add 2')
                    sum += 1

            elif checked_equal == "list_without_first":
                checked_equal = list[1:len(splitted)]

                diffs = []
                checked_equal = splitted[1:len(splitted)]
                for i in range(len(checked_equal)-1):
                    diffs.append(abs(checked_equal[i+1] - checked_equal[i]))
                res = [i for i in diffs if i not in [1, 2, 3]]
                if res == []:
                    print('add 3')

                    sum += 1

                elif check_no_differences(checked_equal):
                    print('add 4')
                    sum += 1

            elif check_equal_plus2(splitted):
                diffs = []
                for i in range(len(splitted)-2):
                    diffs.append(abs(splitted[i+2] - splitted[i]))
                res = [i for i in diffs if i not in [1, 2, 3]]
                if len(res) == 0:
                    print('add 5')
                    sum += 1

    return sum


print(day_2("day_2/input.txt"))

# 337 too low
# 386 too wrong
# 392 too high
# 534 too high
