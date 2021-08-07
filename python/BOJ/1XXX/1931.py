"""
https://www.acmicpc.net/problem/1931
1931.회의실 배정
실버2
풀이1.
"""
import sys

input = sys.stdin.readline
meetings = list()
answer = 0
last_end = 0

for _ in range(int(input())):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

for meeting in meetings:
    if meeting[0] < last_end:
        continue
    last_end = meeting[1]
    answer += 1

print(answer)