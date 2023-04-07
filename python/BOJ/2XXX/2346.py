"""
https://www.acmicpc.net/problem/2346
2346.풍선 터뜨리기
실버3
풀이1.148ms
"""
from collections import deque

N = int(input())
balloons = deque([(x + 1, y) for x, y in enumerate(list(map(int, input().split())))])

while len(balloons):
    num, cnt = balloons.popleft()
    print(num, end=' ')
    if not balloons:
        break
    if cnt > 0:
        for i in range(cnt - 1):
            balloons.append(balloons.popleft())
    else:
        for i in range(-cnt):
            balloons.appendleft(balloons.pop())