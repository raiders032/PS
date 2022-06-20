"""

https://www.acmicpc.net/problem/13413
13413.오셀로 재배치
풀이1.1308ms
"""
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    o1 = input().rstrip()
    o2 = input().rstrip()
    count_wb = 0
    count_bw = 0

    for i in range(len(o1)):
        if o1[i] == o2[i]:
            continue
        if o1[i] == 'W':
            count_wb += 1
        else:
            count_bw += 1

    print(max(count_wb, count_bw))