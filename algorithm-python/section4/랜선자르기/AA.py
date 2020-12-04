K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
left = 0
right = max(arr)
maxL = 0

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for x in arr:
        cnt += x//mid
    if cnt >= N:
        maxL = max(maxL, mid)
        left = mid + 1
    else:
        right = mid - 1
print(maxL)
