"""
https://www.acmicpc.net/problem/11000
11000.강의실 배정
골드5
풀이1.416ms
"""
import sys
import heapq

input = sys.stdin.readline
N = int(input())
time_tables = list()

for _ in range(N):
    start, end = map(int, input().split())
    time_tables.append((start, end))

time_tables.sort()
end_times = list([time_tables[0][1]])

for i in range(1, N):
    if time_tables[i][0] < end_times[0]:
        heapq.heappush(end_times, time_tables[i][1])
        continue
    heapq.heappop(end_times)
    heapq.heappush(end_times, time_tables[i][1])

print(len(end_times))
"""
7
1 3
2 5
4 7
1 8
2 8
7 8
5 9
5
---
3
999999999 1000000000
999999998 999999999 
1 999999998
1
"""