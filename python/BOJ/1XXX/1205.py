"""
https://www.acmicpc.net/problem/1205
1205.등수 구하기
실버5
풀이1.68ms
"""
N, point, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
points = list(map(int, input().split()))
left = 0
right = N - 1
idx = N

while left <= right:
    mid = (left + right) // 2
    if point <= points[mid]:
        left = mid + 1
    else:
        right = mid - 1
        idx = mid

if 0 <= idx < N:
    while idx > 0 and point == points[idx - 1]:
        idx -= 1
    print(idx + 1)
else:
    if N < P:
        while idx > 0 and point == points[idx - 1]:
            idx -= 1
        print(idx + 1)
    else:
        print(-1)

"""
5 2 5
6 5 4 3 1
5
---
9 5 10
10 10 10 9 9 8 7 6 6
10
---
3 90 10
100 100 90
3
"""