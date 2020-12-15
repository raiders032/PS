def findNum(arr, N):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == N:
            return mid
        if arr[mid] < N:
            left = mid + 1
        else:
            right = mid - 1
    return mid


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(findNum(arr, M) + 1)
