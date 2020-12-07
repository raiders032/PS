N, M = input().split()
N = list(N)
M = int(M)
res = 0
for i in range(len(N)):
    for j in range(i+1, min(len(N), i+M+1)):
        if N[i] < N[j]:
            M -= 1
            break
    else:
        res = res * 10 + int(N[i])
print(res // pow(10, M))
