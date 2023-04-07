"""
https://school.programmers.co.kr/learn/courses/30/lessons/92341
주차 요금 계산
풀이1.100점
"""
from collections import defaultdict
import math


def time_to_minutes(time):
    hour, minutes = time.split(':')
    return int(hour) * 60 + int(minutes)


def solution(fees, records):
    answer = []
    car_number_total_time = defaultdict(int)
    car_number_in_time = defaultdict(int)

    for record in records:
        time, car_number, in_out = record.split()

        if in_out == "IN":
            car_number_in_time[car_number] = time_to_minutes(time)
            continue

        car_number_total_time[car_number] += time_to_minutes(time) - car_number_in_time[car_number]
        del car_number_in_time[car_number]

    for car_number, in_time in car_number_in_time.items():
        car_number_total_time[car_number] += time_to_minutes('23:59') - car_number_in_time[car_number]

    print(car_number_total_time)
    result = []
    for car_number, total_time in car_number_total_time.items():
        if total_time <= fees[0]:
            result.append((car_number, fees[1]))
            continue

        result.append((car_number, fees[1] + (math.ceil((total_time - fees[0]) / fees[2]) * fees[3])))

    for car_number, price in sorted(result):
        answer.append(price)

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))