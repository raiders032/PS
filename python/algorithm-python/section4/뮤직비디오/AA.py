N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 1
right = sum(arr)
minLength = right
while left <= right:
    cnt = 1
    mid = (left + right) // 2
    partialSum = 0
    for x in arr:
        partialSum += x
        if partialSum > mid:
            cnt += 1
            partialSum = x
    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1
        minLength = min(minLength, mid)
print(minLength)
