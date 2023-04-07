"""
https://www.acmicpc.net/problem/6996
6996.애너그램
풀이1.72ms
"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = input().split()
    if sorted(list(a)) == sorted(list(b)):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
