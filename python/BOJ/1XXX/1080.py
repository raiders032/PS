"""
https://www.acmicpc.net/problem/1080
1080.행렬
실버2
풀이1.376ms
"""
import sys


def operate(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if mat1[i][j] == '1':
                mat1[i][j] = '0'
            else:
                mat1[i][j] = '1'


def is_same():
    for i in range(N):
        for j in range(M):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True


input = sys.stdin.readline
N, M = map(int, input().split())
mat1 = [list(input().rstrip()) for _ in range(N)]
mat2 = [list(input().rstrip()) for _ in range(N)]
count = 0

if is_same():
    print(0)
    exit()

for i in range(N - 2):
    for j in range(M - 2):
        if mat1[i][j] == mat2[i][j]:
            continue
        count += 1
        operate(i, j)
        if is_same():
            print(count)
            exit()
print(-1)

