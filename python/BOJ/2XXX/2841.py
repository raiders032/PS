"""
https://www.acmicpc.net/problem/2841
2841.외계인의 기타 연주
실버1
풀이3
"""
import sys

input = sys.stdin.readline
N, P = map(int, input().split())
lines = [list() for _ in range(7)]
melody = [tuple(map(int, input().split())) for _ in range(N)]
sheep_count = 0

for number, fret in melody:
    while lines[number] and lines[number][-1] >= fret:
        if lines[number][-1] != fret:
            sheep_count += 1
        else:
            sheep_count -= 1
        lines[number].pop()

    sheep_count += 1
    lines[number].append(fret)

print(sheep_count)