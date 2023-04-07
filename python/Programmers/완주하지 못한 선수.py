"""
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
완주하지 못한 선수
레벨1
풀이1
"""
from collections import defaultdict


def solution(participant, completion):
    name_count = defaultdict(int)

    for name in participant:
        name_count[name] += 1

    for name in completion:
        if name_count[name] == 0:
            return name
        name_count[name] -= 1

    for name, count in name_count.items():
        if count:
            return name
