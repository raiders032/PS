N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
res = [N]
for i in range(1, N):
    res.insert(arr[i], N - i)
for x in res:
    print(x, end=' ')
