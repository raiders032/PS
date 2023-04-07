"""
https://www.acmicpc.net/problem/1744
1744.수 묶기
풀이3.72ms
"""
import sys
input = sys.stdin.readline

N = int(input())
positive_numbers = []
negative_numbers = []
sheep_count = 0
for i in range(N):
    number = int(input())
    if number > 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
positive_numbers.sort(reverse=True)
negative_numbers.sort()

for i in range(0, len(positive_numbers), 2):
    if i + 1 < len(positive_numbers):
        if positive_numbers[i + 1] != 1:
            sheep_count += positive_numbers[i] * positive_numbers[i + 1]
        else:
            sheep_count += positive_numbers[i] + positive_numbers[i + 1]
    else:
        sheep_count += positive_numbers[i]

for i in range(0, len(negative_numbers), 2):
    if i + 1 < len(negative_numbers):
        sheep_count += negative_numbers[i] * negative_numbers[i + 1]
    else:
        sheep_count += negative_numbers[i]

print(sheep_count)