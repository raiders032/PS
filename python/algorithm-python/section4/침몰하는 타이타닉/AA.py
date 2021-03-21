N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
left = 0
right = N-1
while left <= right:
    if left == right:
        cnt += 1
        break
    if arr[left] + arr[right] <= M:
        left += 1
        right -= 1
    else:
        right -= 1
    cnt += 1
print(cnt)
