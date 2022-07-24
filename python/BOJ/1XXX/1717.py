"""
https://www.acmicpc.net/problem/1717
1717.집합의 표현
풀이1.364ms
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def get_parent(node):
    if disjoint_set[node] == node:
        return node
    disjoint_set[node] = get_parent(disjoint_set[node])
    return disjoint_set[node]


def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    if parent_a < parent_b:
        disjoint_set[parent_b] = parent_a
    else:
        disjoint_set[parent_a] = parent_b


N, M = map(int, input().split())
disjoint_set = [i for i in range(N + 1)]

for _ in range(M):

    opcode, a, b = map(int, input().split())
    if opcode == 0:
        union(a, b)
    else:
        print("YES" if get_parent(a) == get_parent(b) else "NO")
