N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
for _ in range(M):
    arr[N-1] -= 1
    arr[0] += 1

    idx = N-2
    while True:
        if arr[N-1] < arr[idx]:
            idx -= 1
            continue
        break
    arr[N-1], arr[idx+1] = arr[idx+1], arr[N-1]

    idx = 1
    while True:
        if arr[0] > arr[idx]:
            idx += 1
            continue
        break
    arr[0], arr[idx-1] = arr[idx-1], arr[0]
print(arr[N-1] - arr[0])
