def reverse(x):
    res = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        res = res * 10 + digit
    return res

def isPrime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    if x == 1:
        return False
    return True

n = int(input())
arr = list(map(int, input().split()))
for x in arr:
    reversedX = reverse(x)
    if isPrime(reversedX):
        print(reversedX, end=' ')
