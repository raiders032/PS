isPrime = [True] * 10001
isPrime[1] = False
for i in range(2, 10001):
    if isPrime[i] == False:
        continue
    for j in range(2*i, 10001, i):
        isPrime[j] = False
M = int(input())
N = int(input())
sum = 0
minN = 10000000
isOk = False
for i in range(M, N+1):
    if isPrime[i]:
        isOk = True
        minN = min(minN, i)
        sum += i
if isOk:
    print(sum)
    print(minN)
else:
    print('-1')
