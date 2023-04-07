"""
https://www.acmicpc.net/problem/17451
17451.평행 우주
실버3
풀이2.372ms
"""
import sys

input = sys.stdin.readline

N = int(input())
velocity = list(map(int, input().split()))
velocity = velocity[::-1]
sheep_count = velocity[0]

for i in range(N - 1):
    if sheep_count <= velocity[i + 1]:
        sheep_count = velocity[i + 1]
    else:
        sheep_count = sheep_count // velocity[i + 1] + (1 if sheep_count % velocity[i + 1] else 0)
        sheep_count *= velocity[i + 1]

print(sheep_count)
