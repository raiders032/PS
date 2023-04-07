"""
https://www.acmicpc.net/problem/2138
2138.전구와 스위치
실버1
풀이1.180ms
"""
import sys

input = sys.stdin.readline


def get_count(count):
    for i in range(1, n):
        if source[i - 1] != target[i - 1]:
            count += 1
            source[i - 1] = (source[i - 1] + 1) % 2
            source[i] = (source[i] + 1) % 2
            if i < n - 1:
                source[i + 1] = (source[i + 1] + 1) % 2
    if source != target:
        count = sys.maxsize
    return count


n = int(input())
original = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

source = list(original)
result1 = get_count(0)

source = list(original)
source[0] = (source[0] + 1) % 2
source[1] = (source[1] + 1) % 2
result2 = get_count(1)

print(min(result1, result2) if min(result1, result2) != sys.maxsize else -1)
