"""
https://www.acmicpc.net/problem/2164
2164.카드2
실버4
풀이2.256ms
"""
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while len(deque) >= 2:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])