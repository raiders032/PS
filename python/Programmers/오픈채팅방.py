"""
https://programmers.co.kr/learn/courses/30/lessons/42888
오픈채팅방
레벨2
"""


def solution(record):
    answer = []
    id_nickname = dict()
    records = []
    for string in record:
        if string.startswith('Enter'):
            command, id, nickname = string.split()
            id_nickname[id] = nickname
            records.append((id, "님이 들어왔습니다."))
        elif string.startswith('Leave'):
            command, id = string.split()
            records.append((id, "님이 나갔습니다."))
        else:
            command, id, nickname = string.split()
            id_nickname[id] = nickname

    for id, command in records:
        answer.append(id_nickname[id] + command)

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))