"""
https://www.acmicpc.net/problem/1931
1931.회의실 배정
실버2
풀이2.324ms
"""
import sys

input = sys.stdin.readline

N = int(input())
meetings = []
answer = 0

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

last_end = 0
for (start, end) in meetings:
    if last_end <= start:
        answer += 1
        last_end = end

print(answer)