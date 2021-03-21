def getBin(x):
    if x == 0:
        return ''
    return str(getBin(x//2)) + str(x % 2)


print(getBin(int(input())))
