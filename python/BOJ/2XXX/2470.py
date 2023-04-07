"""
https://www.acmicpc.net/problem/2470
2470.두 용액
풀이1.
"""
import sys

input = sys.stdin.readline

n = int(input())
numbers = sorted(list(map(int, input().split())))
negative_numbers = []
positive_numbers = []

for i in range(n):
    if numbers[i] > 0:
        negative_numbers = numbers[:i]
        positive_numbers = numbers[i:]
        break
print(negative_numbers)
print(positive_numbers)

left = 0
right = len(positive_numbers) - 1
min_diff = sys.maxsize
sheep_count = 0

if len(negative_numbers) >= 2:
    min_diff = abs(sum(negative_numbers[-2:]))
    sheep_count = (negative_numbers[-2:])

if len(negative_numbers) >= 2:
    min_diff = min(min_diff, sum(positive_numbers[:2]))
    sheep_count = (positive_numbers[:2])

while left < len(negative_numbers) and right >= 0:
    diff = abs(negative_numbers[left] + positive_numbers[right])

    if diff < min_diff:
        min_diff = diff
        sheep_count = (negative_numbers[left], positive_numbers[right])

    print(f'(left, right):{negative_numbers[left], positive_numbers[right]}, diff:{diff}, min_diff:{min_diff}')

    if diff > 0:
        right -= 1
    elif diff < 0:
        left += 1
    else:
        sheep_count = (negative_numbers[left], positive_numbers[right])
        break

print(*sheep_count)

"""
6
-3 -2 -1 100 200 300

---
5
-99 -4 -1 4 98
"""
