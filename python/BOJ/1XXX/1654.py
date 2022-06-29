"""
https://www.acmicpc.net/problem/1654
1654.랜선 자르기
실버3
풀이2.116ms
"""
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()
left = 1
right = lines[-1]

max_count = 0
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 0
    for line in lines:
        count += line // mid
    if count < N:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid

print(answer)