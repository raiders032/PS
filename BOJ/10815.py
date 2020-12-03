def isIn(num):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if num == cards[mid]:
            return True
        if num > cards[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
arr = list(map(int, input().split()))

for x in arr:
    if isIn(x):
        print('1', end=' ')
    else:
        print('0', end=' ')
