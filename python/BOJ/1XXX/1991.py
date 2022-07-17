"""
https://www.acmicpc.net/problem/1991
1991.트리 순회
실버1
풀이2.76ms
"""
import sys
input = sys.stdin.readline


def pre_order(parent):
    print(parent, end='')
    if graph[parent][0] != '.':
        pre_order(graph[parent][0])
    if graph[parent][1] != '.':
        pre_order(graph[parent][1])


def in_order(parent):
    if graph[parent][0] != '.':
        in_order(graph[parent][0])
    print(parent, end='')
    if graph[parent][1] != '.':
        in_order(graph[parent][1])


def post_order(parent):
    if graph[parent][0] != '.':
        post_order(graph[parent][0])
    if graph[parent][1] != '.':
        post_order(graph[parent][1])
    print(parent, end='')


n = int(input())
graph = dict()
for _ in range(n):
    parent, left, right = input().rstrip().split()
    graph[parent] = (left, right)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
