"""
https://www.acmicpc.net/problem/12891
12891.DNA 비밀번호
실버2
풀이1.984ms
"""
from collections import Counter
from collections import defaultdict


def is_valid_password():
    for i in range(4):
        if counts[DNA[i]] < conditions[DNA[i]]:
            return False
    return True


S, P = map(int, input().split())
DNA_string = input()
counts = Counter(DNA_string[:P])

DNA = ['A', 'C', 'G', 'T']
conditions = defaultdict(int)
for index, condition in enumerate(map(int, input().split())):
    conditions[DNA[index]] = condition

sheep_count = 0
left = 0
right = P - 1
while True:
    if is_valid_password():
        sheep_count += 1
    counts[DNA_string[left]] -= 1
    left += 1
    right += 1
    if right >= S:
        break
    counts[DNA_string[right]] += 1

print(sheep_count)