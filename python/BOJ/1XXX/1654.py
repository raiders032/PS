"""
https://www.acmicpc.net/problem/1654
1654.랜선 자르기
실버3
풀이1.132ms
"""
import sys

input = sys.stdin.readline
K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]
left = 1
right = 2 ** 31 - 1
ans = 1

while left <= right:
    mid = (left + right) // 2
    count = 0

    for num in nums:
        count += num // mid

    if count < N:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid

print(ans)