"""
https://www.acmicpc.net/problem/10819
10819.차이를 최대로
풀이1.176ms
"""
import sys
import itertools

input = sys.stdin.readline
N = int(input())
answer = -sys.maxsize

for numbers in itertools.permutations(list(map(int, input().split()))):
    result = 0
    for i in range(N - 1):
        result += abs(numbers[i] - numbers[i + 1])
    answer = max(answer, result)

print(answer)