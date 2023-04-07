"""
https://www.acmicpc.net/problem/16960
16960.스위치와 램프
실버4
풀이1.76ms
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
switches = [list(map(int, input().split()))[1:] for _ in range(N)]
count = [0] * (M + 1)
for switch in switches:
    for lamp in switch:
        count[lamp] += 1

sheep_count = 0
for switch in switches:
    is_redundant = True

    for lamp in switch:
        if count[lamp] == 1:
            is_redundant = False
            break

    if is_redundant:
        sheep_count = 1
        break
print(sheep_count)