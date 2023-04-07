"""
https://school.programmers.co.kr/learn/courses/30/lessons/72414
광고 삽입
풀이1.
"""


def hhmmss_to_seconds(hhmmss):
    hour, minute, second = hhmmss.split(':')
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def seconds_to_hhmmss(seconds):
    result = ''
    result += str(seconds // 3600).zfill(2) + ':'
    seconds %= 3600
    result += str(seconds // 60).zfill(2) + ':'
    seconds %= 60
    result += str(seconds).zfill(2)
    return result


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    n = hhmmss_to_seconds(play_time)
    d = [0] * (n + 2)

    for log in logs:
        start, end = map(hhmmss_to_seconds, log.split('-'))
        d[start] += 1
        d[end] -= 1

    for i in range(1, n + 1):
        d[i] += d[i - 1]

    adv_time_unit = hhmmss_to_seconds(adv_time)
    count = sum(d[:adv_time_unit])
    max_count = count

    answer = 0
    for i in range(1, n - adv_time_unit + 1):
        count = count - d[i - 1] + d[i + adv_time_unit - 1]
        if max_count < count:
            max_count = count
            answer = i

    return seconds_to_hhmmss(answer)


print(solution("02:03:55",
               "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))

print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))

print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
