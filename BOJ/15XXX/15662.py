"""
21.01.22/560ms
15662.톱니바퀴 (2)
실버2
"""
from collections import deque
import sys


def rotate(num, dir):
    if dir == 1:
        gears[num].appendleft(gears[num].pop())
    elif dir == -1:
        gears[num].append(gears[num].popleft())


input = sys.stdin.readline
N = int(input())
gears = [deque(map(int, input().rstrip())) for _ in range(N)]
K = int(input())
res = 0

for _ in range(K):
    num, dir = map(int, input().split())
    dirs = [0] * N
    dirs[num - 1] = dir
    for i in range(num, N):
        if gears[i][6] != gears[i - 1][2]:
            dirs[i] = dirs[i - 1] * -1
    for i in range(num - 2, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            dirs[i] = dirs[i + 1] * -1
    for i in range(N):
        rotate(i, dirs[i])
for i in range(N):
    if gears[i][0] == 1:
        res += 1
print(res)
