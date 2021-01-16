n = input()
length = len(n)
n = int(n)
res = 0

for i in range(1, length+1):
    if pow(10, i) <= n:
        res += i * (pow(10, i) - pow(10, i-1))
    else:
        res += i * (n - pow(10, i-1) + 1)
print(res)
