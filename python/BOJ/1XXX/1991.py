"""
https://www.acmicpc.net/problem/1991
1991.트리 순회
실버1
풀이1.72ms
"""
import sys

input = sys.stdin.readline
N = int(input())
tree = dict()


def pre_order(parent):
    print(parent, end='')
    if tree[parent][0] != '.':
        pre_order(tree[parent][0])
    if tree[parent][1] != '.':
        pre_order(tree[parent][1])


def in_order(parent):
    if tree[parent][0] != '.':
        in_order(tree[parent][0])
    print(parent, end='')
    if tree[parent][1] != '.':
        in_order(tree[parent][1])


def post_order(parent):
    if tree[parent][0] != '.':
        post_order(tree[parent][0])
    if tree[parent][1] != '.':
        post_order(tree[parent][1])
    print(parent, end='')


for _ in range(N):
    parent, left_child, right_child = input().split()
    tree[parent] = (left_child, right_child)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
