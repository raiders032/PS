"""
https://www.acmicpc.net/problem/18258
18258.큐 2
실버4
풀이1.2016ms
"""
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
q = deque()

for _ in range(N):
    command = input().rstrip()

    if command.startswith('push'):
        command, X = command.split()
        q.append(X)
    elif command.startswith('pop'):
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command.startswith('front'):
        if q:
            print(q[0])
        else:
            print(-1)
    elif command.startswith('back'):
        if q:
            print(q[-1])
        else:
            print(-1)
    elif command.startswith('size'):
        print(len(q))
    elif command.startswith('empty'):
        if q:
            print(0)
        else:
            print(1)