"""
https://www.acmicpc.net/problem/1072
1072.게임
실버3
풀이1.80ms
"""
import math

X, Y = map(int, input().split())
Z = math.trunc(Y * 100 / X)
left = 0
right = 1000000000
ans = -1
while left <= right:
    mid = (left + right) // 2
    z = math.trunc((Y + mid) * 100 / (X + mid))
    if Z == z:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
print(ans)
