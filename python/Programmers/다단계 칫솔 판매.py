"""
https://school.programmers.co.kr/learn/courses/30/lessons/77486
다단계 칫솔 판매
풀이1.100점
"""
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    def share_income(child, income):
        if child == '-':
            return

        if int(income * 0.1) < 1:
            name_income[child] += income
        else:
            name_income[child] += income - int(income * 0.1)
            share_income(parent[child], int(income * 0.1))

    answer = []
    parent = dict()
    name_income = defaultdict(int)

    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]

    for i in range(len(seller)):
        share_income(seller[i], amount[i] * 100)

    for name in enroll:
        answer.append(name_income[name])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))