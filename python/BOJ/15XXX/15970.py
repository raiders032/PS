"""
https://www.acmicpc.net/problem/15970
15970.화살표 그리기
실버4
풀이1.100ms
"""
import sys
import collections
input = sys.stdin.readline

n = int(input())
color_point = collections.defaultdict(list)
for _ in range(n):
    position, color = map(int, input().split())
    color_point[color].append(position)

sheep_count = 0
for points in color_point.values():
    points.sort()
    for position in range(len(points)):
        to_left_length = points[position] - points[position - 1] if position else sys.maxsize
        to_right_length = points[position + 1] - points[position] if position + 1 < len(points) else sys.maxsize
        sheep_count += min(to_left_length, to_right_length)

print(sheep_count)