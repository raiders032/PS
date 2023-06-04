"""
https://www.acmicpc.net/problem/22856
22856.트리 순회
풀이2.296ms
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def traversal_all(node):
    global count
    if tree[node][0] != -1:
        count += 2
        traversal_all(tree[node][0])

    if tree[node][1] != -1:
        count += 2
        traversal_all(tree[node][1])


def traversal_right(node):
    global count

    if tree[node][1] != -1:
        count -= 1
        traversal_right(tree[node][1])


n = int(input())
tree = dict()
for _ in range(n):
    parent, left_child, right_child = map(int, input().split())
    tree[parent] = (left_child, right_child)

count = 0
traversal_all(1)
traversal_right(1)
print(count)