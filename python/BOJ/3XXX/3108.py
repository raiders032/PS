"""
https://www.acmicpc.net/problem/3108
3108.로고
풀이1.160ms
"""
import sys
input = sys.stdin.readline


def find(node):
    if root[node] != node:
        root[node] = find(root[node])

    return root[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 <= root2:
        root[root2] = root1
    else:
        root[root1] = root2


def check(i, j):
    x1, y1, x2, y2 = squares[i]
    x3, y3, x4, y4 = squares[j]

    if x3 < x1 <= x2 < x4 and y3 < y1 <= y2 < y4:
        return False

    if x1 < x3 <= x4 < x2 and y1 < y3 <= y4 < y2:
        return False

    if y2 < y3 or y4 < y1 or x4 < x1 or x2 < x3:
        return False

    return True


n = int(input())
root = [i for i in range(n + 1)]
squares = [[0, 0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n + 1):
        if check(i, j):
            union(i, j)

for i in range(n + 1):
    find(i)

print(len(set(root)) - 1)