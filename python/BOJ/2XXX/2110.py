"""
https://www.acmicpc.net/problem/2110
2110.공유기 설치
풀이2.500ms
"""
import sys

input = sys.stdin.readline
N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]
homes.sort()

left = 0
right = 2000000000
answer = 0

while left <= right:
    mid = (left + right) // 2

    is_possible = True
    for i in range(N - 1):
        if homes[i + 1] - homes[i] < mid:
            is_possible = False
            break

    if is_possible:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)


