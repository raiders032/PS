"""
https://www.acmicpc.net/problem/2164
2164.카드2
실버4
풀이1.244ms
"""
from collections import deque

N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])