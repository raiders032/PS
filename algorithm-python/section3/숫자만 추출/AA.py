def get_number(string):
    res = 0
    for c in string:
        if c.isdigit():
            res = res * 10 + int(c)
    return res


def get_divisor(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt


string = input()
num = get_number(string)
print(num)
print(get_divisor(num))
