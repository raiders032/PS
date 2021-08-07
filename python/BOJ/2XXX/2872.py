"""
https://www.acmicpc.net/problem/2872
2872.우리집엔 도서관이 있어
실버3
풀이1.220ms
"""
import sys

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
idx = N - 1
ans = N

for idx in range(N - 1, -1, -1):
    if nums[idx] == N:
        ans -= 1
        N -= 1
print(ans)
