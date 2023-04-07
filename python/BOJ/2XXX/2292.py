"""
https://www.acmicpc.net/problem/2292
2292.벌집
브론즈2
풀이2.84ms
"""
N = int(input())
sheep_count = 1
start = end = 1

while end < N:
    start = end + 1
    end = start + sheep_count * 6 - 1
    sheep_count += 1

print(sheep_count)