"""
https://school.programmers.co.kr/learn/courses/30/lessons/17678
[1차] 셔틀버스
풀이1.
"""


def HHMM_to_minutes(HHMM):
    hour, minutes = map(int, HHMM.split(':'))
    return hour * 60 + minutes


def minutes_to_HHMM(minutes):
    hh = minutes // 60
    hh = str(hh) if len(str(hh)) == 2 else '0' + str(hh)
    mm = minutes % 60
    mm = str(mm) if len(str(mm)) == 2 else '0' + str(mm)
    return ''.join([hh, ':', mm])


def solution(n, t, m, timetable):
    timetable = list(map(HHMM_to_minutes, timetable))
    timetable.sort()
    current_bus_time = HHMM_to_minutes('09:00')
    person_count = 0
    bus_count = 1
    i = 0
    last_person = 0

    while bus_count <= n and i < len(timetable):
        if person_count == m:
            bus_count += 1
            current_bus_time += t
            person_count = 0
            continue

        if timetable[i] <= current_bus_time:
            person_count += 1
            last_person = timetable[i]
            i += 1
        else:
            bus_count += 1
            current_bus_time += t
            person_count = 0

    print(f'bus_count:{bus_count}, current_bus_time:{current_bus_time}, person_count:{person_count}, last_person:{last_person}')

    if person_count == 0:
        return minutes_to_HHMM(current_bus_time - t)
    elif person_count < m:
        return minutes_to_HHMM(current_bus_time)
    else:
        return minutes_to_HHMM(last_person - 1)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
