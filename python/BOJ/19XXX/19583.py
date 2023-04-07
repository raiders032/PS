"""
https://www.acmicpc.net/problem/19583
19583.싸이버개강총회
풀이1.356ms
"""
import sys
from collections import defaultdict

input = sys.stdin.readline
times = list(map(lambda x: int(''.join(x.split(':'))), input().rstrip().split()))
name_attendance = defaultdict(set)
count = 0

while True:
    time_name = input().rstrip()

    if not time_name:
        break

    time, name = time_name.split()
    time = int(''.join(time.split(':')))

    if len(name_attendance[name]) == 2:
        continue

    if time <= times[0]:
        name_attendance[name].add('start')

    if times[1] <= time <= times[2]:
        name_attendance[name].add('end')

    if len(name_attendance[name]) == 2:
        count += 1

print(count)