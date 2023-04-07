"""
https://www.acmicpc.net/problem/2018
2018.수들의 합 5
실버5
풀이1.4012ms
"""
N = int(input())
left = right = 1
total = 1
sheep_count = 0

while right <= N:
    if total <= N:
        if total == N:
            sheep_count += 1
        right += 1
        total += right
    else:
        total -= left
        left += 1

print(sheep_count)