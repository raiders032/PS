"""
https://www.acmicpc.net/problem/7511
7511.소셜 네트워킹 어플리케이션
풀이1.952ms
"""
import sys

input = sys.stdin.readline


def find(vertex):
    if disjoint_set[vertex] != vertex:
        disjoint_set[vertex] = find(disjoint_set[vertex])

    return disjoint_set[vertex]


def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)

    if root1 <= root2:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root1] = root2


for i in range(int(input())):
    print("Scenario " + str(i + 1) + ":")
    n = int(input())
    disjoint_set = [i for i in range(n + 1)]

    for _ in range(int(input())):
        a, b = map(int, input().split())
        union(a, b)

    for _ in range(int(input())):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print("1")
        else:
            print("0")
    print()