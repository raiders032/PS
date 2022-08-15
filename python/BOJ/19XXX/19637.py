"""
https://www.acmicpc.net/problem/19637
19637.IF문 좀 대신 써줘
풀이1.620ms
"""
import sys
input = sys.stdin.readline


def get_name(power):
    left = 0
    right = len(name_power) - 1
    name = ''

    while left <= right:
        mid = (left + right) // 2
        if power <= name_power[mid][1]:
            name = name_power[mid][0]
            right = mid - 1
        else:
            left = mid + 1

    return name


n, m = map(int, input().split())
name_power = []
existent_power = set()
for _ in range(n):
    name, power = input().split()
    if power in existent_power:
        continue
    name_power.append((name, int(power)))
    existent_power.add(power)

for _ in range(m):
    power = int(input())
    print(get_name(power))