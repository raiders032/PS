"""
https://www.acmicpc.net/problem/1966
프린터 큐
실버3
풀이1.92ms
"""
from collections import deque
import sys

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    queue = deque()
    N, index = map(int, input().split())
    count = 1
    max_num = 0

    for i, number in enumerate(map(int, input().split())):
        max_num = max(max_num, number)
        queue.append((i, number))

    while queue:
        if queue[0][1] == max_num:
            if queue[0][0] == index:
                print(count)
                break
            queue.popleft()
            count += 1
            max_num = max(queue, key=lambda x: x[1])[1]
        else:
            queue.append(queue.popleft())