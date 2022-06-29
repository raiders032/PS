"""
https://www.acmicpc.net/problem/1654
1654.랜선 자르기
실버3
풀이2.116ms
"""
import sys

input = sys.stdin.readline
K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]
left = 1
right = 2 ** 31 - 1
ans = 0

while left <= right:
    count = 0
    mid = (left + right) // 2
    for num in nums:
        count += num // mid

    if count >= N:
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)
