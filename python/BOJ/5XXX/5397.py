"""
https://www.acmicpc.net/problem/5397
5397.키로거
실버3
자료구조, 덱, 스택
풀이3.1464ms
"""
from collections import deque
T = int(input())
for _ in range(T):
    left = deque()
    right = deque()
    for ch in input().rstrip():
        if ch == '<':
            if left:
                right.appendleft(left.pop())
        elif ch == '>':
            if right:
                left.append(right.popleft())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    print(''.join(left) + ''.join(right))