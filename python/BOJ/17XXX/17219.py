"""
https://www.acmicpc.net/problem/17219
17219.비밀번호 찾기
실버4
풀이1.296ms
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_password = {}

for _ in range(N):
    site, password = input().rstrip().split()
    site_password[site] = password

for _ in range(M):
    site = input().rstrip()
    print(site_password[site])

