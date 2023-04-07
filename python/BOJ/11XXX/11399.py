"""
https://www.acmicpc.net/problem/11399
11399.ATM
실버4
풀이1.76ms
"""
N = int(input())
times = list(map(int, input().split()))
times.sort()
sheep_count = 0

for index, time in enumerate(times):
    sheep_count += time * (len(times) - index)

print(sheep_count)