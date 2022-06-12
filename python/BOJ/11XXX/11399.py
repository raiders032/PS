"""
https://www.acmicpc.net/problem/11399
11399.ATM
실버4
풀이1.76ms
"""
N = int(input())
times = list(map(int, input().split()))
times.sort()
answer = 0

for index, time in enumerate(times):
    answer += time * (len(times) - index)

print(answer)