def getCnt(length):
    cnt = 1
    end = arr[0]
    for i in range(1, N):
        if arr[i]-end >= length:
            cnt += 1
            end = arr[i]
    return cnt


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

res = 0
left = 1
right = arr[N-1]
while left <= right:
    mid = (left + right) // 2
    if getCnt(mid) >= C:
        left = mid + 1
        res = mid
    else:
        right = mid - 1
print(res)
