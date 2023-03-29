"""
https://www.acmicpc.net/problem/1300
1300.k번째 수
풀이1.1164ms
"""
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

low = 0
high = n * n

while low + 1 < high:
    mid = (low + high) // 2
    count = 0

    for i in range(1, n + 1):
        count += min(n, mid // i)

    if count >= k:
        high = mid
    else:
        low = mid

print(high)