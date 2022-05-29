list1 = [8,2,3,0,7]


def sumOfList(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size - 1] + sumOfList(lst, size - 1)


# Driver code
total = sumOfList(list1, len(list1))

print(total)