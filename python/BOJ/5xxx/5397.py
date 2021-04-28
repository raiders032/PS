"""
https://www.acmicpc.net/problem/5397
5397.키로거
실버3
자료구조, 덱, 스택
풀이1.1280ms
"""
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    left = deque()
    right = deque()
    for char in list(input().rstrip()):
        if char == '<':
            if not left:
                continue
            right.appendleft(left.pop())
        elif char == '>':
            if not right:
                continue
            left.append(right.popleft())
        elif char == '-':
            if not left:
                continue
            left.pop()
        else:
            left.append(char)

    print(''.join(left + right))
