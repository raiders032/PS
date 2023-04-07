"""
https://www.acmicpc.net/problem/1043
1043.거짓말
풀이1.68ms
"""
import sys
input = sys.stdin.readline


def find(node):
    if disjoint_set[node] != node:
        disjoint_set[node] = find(disjoint_set[node])
    return disjoint_set[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 <= root2:
        disjoint_set[root2] = disjoint_set[root1]
    else:
        disjoint_set[root1] = disjoint_set[root2]


N, M = map(int, input().split())
true_people = list(map(int, input().split()))
if true_people[0] == 0:
    print(M)
    exit(0)

disjoint_set = [i for i in range(N + 1)]
for i in range(1, true_people[0]):
    union(true_people[i], true_people[i + 1])

parties = [list(map(int, input().split())) for _ in range(M)]
for party in parties:
    people = party[1:]
    for i in range(len(people) - 1):
        union(people[i], people[i + 1])

sheep_count = 0
for party in parties:
    can_lie = True
    people = party[1:]
    for person in people:
        if find(person) == find(true_people[1]):
            can_lie = False
            break

    if can_lie:
        sheep_count += 1
print(sheep_count)
"""
4 3
1 1
2 1 2
1 3
3 2 3 4
0
---
4 3
1 3
2 1 2
1 3
3 2 3 4
0
---
4 5
1 1
1 1
1 2
1 3
2 4 2
2 4 1
1
"""
