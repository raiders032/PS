"""
https://www.acmicpc.net/problem/18114
18114.블랙 프라이데이
풀이1.80ms
"""
import sys


def binary_search(numbers, target):
    low = -1
    high = len(numbers) - 1

    while low + 1 < high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid
        else:
            high = mid

    if numbers[high] != target:
        return -1

    return high


input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0

if binary_search(numbers, M) != -1:
    answer = 1

if not answer:
    left = 0
    right = N - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == M:
            answer = 1
            break

        index = binary_search(numbers, M - sum)
        if numbers[index] != numbers[left] and numbers[index] != numbers[right]:
            answer = 1
            break

        if sum < M:
            left += 1
        else:
            right -= 1

print(answer)
