"""
https://www.acmicpc.net/problem/3151
3151.합이 0
풀이1.
"""
import sys
input = sys.stdin.readline


def binary_search_upper_bound(numbers, number):
    low = -1
    high = len(numbers)

    while low + 1 < high:
        mid = (low + high) // 2
        if numbers[mid] <= number:
            low = mid
        else:
            high = mid

    return high


def binary_search_lower_bound(numbers, number):
    low = -1
    high = len(numbers)

    while low + 1 < high:
        mid = (low + high) // 2
        if numbers[mid] < number:
            low = mid
        else:
            high = mid

    return high


n = int(input())
numbers = sorted(list(map(int, input().split())))
answer = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        target = -(numbers[i] + numbers[j])
        upper_bound = binary_search_upper_bound(numbers[j + 1:], target)
        lower_bound = binary_search_lower_bound(numbers[j + 1:], target)
        answer += upper_bound - lower_bound

print(answer)