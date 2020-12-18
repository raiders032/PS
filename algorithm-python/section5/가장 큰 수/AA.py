N, M = map(int, input().split())
N = list(map(int, str(N)))
stack = []
res = 0
for x in N:
    while M > 0 and stack and stack[-1] < x:
        stack.pop()
        M -= 1
    stack.append(x)
for x in stack:
    res = res * 10 + x
print(res // pow(10, M))
