"""
20055.컨베이어 벨트 위의 로봇
실버1
구현, 시뮬레이션
풀이1. 시간초과
"""
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))
res = 0
isRobot = [False] * N

while conveyor_belt.count(0) < K:
    conveyor_belt.appendleft(conveyor_belt.pop())
    for i in range(N - 2, -1, -1):
        isRobot[i + 1] = isRobot[i]
    isRobot[0] = False

    for i in range(N - 1, -1, -1):
        if not isRobot[i]:
            continue
        if i == N - 1:
            isRobot[i] = False
            continue
        if isRobot[i + 1] or conveyor_belt[i + 1] == 0:
            continue

        conveyor_belt[i + 1] -= 1
        isRobot[i + 1] = True
        isRobot[i] = False

    if not isRobot[0] and conveyor_belt[0]:
        isRobot[0] = True
        conveyor_belt[0] -= 1

    res += 1

print(res)
