"""
https://www.acmicpc.net/problem/5397
5397.키로거
실버3
자료구조, 덱, 스택
풀이4.1292ms
"""
import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
    left = deque()
    right = deque()
    password = input().rstrip()

    for char in password:
        if char == '<':
            if left:
                right.appendleft(left.pop())
        elif char == '>':
            if right:
                left.append(right.popleft())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)

    print(''.join(left + right))
