"""
https://www.acmicpc.net/problem/2231
2231.분해합
브론즈2
풀이1.
"""
N = int(input())
for num in range(1, 1000001):
    if N == (num + sum(list(map(int, list(str(num)))))):
        print(num)
        break
else:
    print(0)
