from collections import defaultdict
import re


def solution(info, query):
    answer = []
    conditions = [['cpp', 'java', 'python'], ['backend', 'frontend'], ['junior', 'senior'], ['chicken', 'pizza']]

    conditions_score = defaultdict(list)
    for i in info:
        condition = i.split()
        conditions_score[tuple(condition[:4])].append(condition[4])

    for q in query:
        q = re.sub('and', '', q)
        keys = []
        target_score = 0
        for i, condition in enumerate(re.findall(r'\S+', q)):
            if condition.isdigit():
                target_score = int(condition)
            elif condition == '-':
                keys.append(conditions[i])
            else:
                keys.append([condition])

        count = 0
        for language in keys[0]:
            for back_front in keys[1]:
                for junior_senior in keys[2]:
                    for pizza_chicken in keys[3]:
                        for score in conditions_score[(language, back_front, junior_senior, pizza_chicken)]:
                            if int(score) >= target_score:
                                count += 1
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] ))