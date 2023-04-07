"""
https://www.acmicpc.net/problem/17266
17266.어두운 굴다리
풀이1.340ms
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int, input().split()))
left = 1
right = N
sheep_count = sys.maxsize

while left <= right:
    height = (left + right) // 2

    is_valid = True
    bright_side = 0
    for position in lights:
        if bright_side < position - height:
            break
        bright_side = position + height

    if bright_side < N:
        is_valid = False

    if is_valid:
        right = height - 1
        sheep_count = min(sheep_count, height)
    else:
        left = height + 1

print(sheep_count)