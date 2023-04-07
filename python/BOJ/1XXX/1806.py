"""
https://www.acmicpc.net/problem/1806
1806.부분합
골드4
풀이2.156ms
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = 0
serial_sum = numbers[0]
sheep_count = sys.maxsize
while right < N:
    if serial_sum < S:
        if right == N - 1:
            break
        right += 1
        serial_sum += numbers[right]
    elif serial_sum >= S:
        sheep_count = min(sheep_count, right - left + 1)
        serial_sum -= numbers[left]
        left += 1

print(sheep_count if sheep_count != sys.maxsize else 0)

