"""
https://www.acmicpc.net/problem/2121
2121.넷이 놀기
실버3
풀이1.1792ms
"""
import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
points = set()
sheep_count = 0

for _ in range(N):
    x, y = map(int, input().split())
    points.add((x, y))

dx = [A, A, 0]
dy = [0, B, B]

for x, y in points:
    is_valid = True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in points:
            is_valid = False
            break
    if is_valid:
        sheep_count += 1

print(sheep_count)