"""
https://www.acmicpc.net/problem/16434
16434.드래곤 앤 던전
풀이1.1356ms
"""
import sys
import math

input = sys.stdin.readline

n, attack = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(n)]


def bi_search(start, end):
    low = start - 1
    high = end

    while low + 1 < high:
        mid = (low + high) // 2
        if determine(mid):
            high = mid
        else:
            low = mid

    return high


def determine(max_hp):
    is_valid = True
    current_hp = max_hp
    current_attack = attack

    for t, a, h in rooms:
        if t == 1:
            current_hp -= (math.ceil(h / current_attack) - 1) * a
            if current_hp <= 0:
                is_valid = False
                break
        else:
            current_attack += a
            current_hp = min(max_hp, current_hp + h)

    return is_valid


start = 1
end = 1

while not determine(end):
    start = end
    end *= 2

print(bi_search(start, end))