"""
14891.톱니바퀴
실버1
구현
풀이1 88ms
"""
from collections import deque
import sys


def rotate_gear(num, dir):
    if dir == 1:
        gears[num].appendleft(gears[num].pop())
    elif dir == -1:
        gears[num].append(gears[num].popleft())


input = sys.stdin.readline
gears = [deque(map(int, list(input().rstrip()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    N, D = map(int, input().split())
    N -= 1
    dirs = [0] * 4
    dirs[N] = D

    for right in range(N + 1, 4):
        if gears[right - 1][2] != gears[right][6]:
            dirs[right] = dirs[right - 1] * -1
        else:
            break

    for left in range(N - 1, -1, -1):
        if gears[left][2] != gears[left + 1][6]:
            dirs[left] = dirs[left + 1] * -1
        else:
            break

    for num in range(4):
        rotate_gear(num, dirs[num])

res = 0
score = [1, 2, 4, 8]
for i in range(4):
    if gears[i][0] == 1:
        res += score[i]
print(res)
