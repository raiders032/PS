"""
https://www.acmicpc.net/problem/7579
7579.앱
골드3
풀이1.
"""
import sys

N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
dp = [[sys.maxsize] * (M + 1) for _ in range(N + 1)]
