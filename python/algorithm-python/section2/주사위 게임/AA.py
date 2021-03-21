def price(x1, x2, x3):
    if(x1 == x2 == x3):
        return 10000+x1*1000
    if(x1 == x2 != x3):
        return 1000 + x1 * 100
    if(x1 != x2 == x3):
        return 1000 + x2 * 100
    else:
        return max(x1, x2, x3) * 100

n = int(input())
max_n = 0
for i in range(n):
    x1, x2, x3 = map(int, input().split())
    max_n = max(max_n, price(x1, x2, x3))
print(max_n)