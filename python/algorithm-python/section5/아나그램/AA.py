str1 = list(input())
str2 = list(input())
dic1 = dict()
dic2 = dict()

for x in str1:
    dic1[x] = dic1.get(x, 0) + 1

for x in str2:
    dic2[x] = dic2.get(x, 0) + 1

for key, val in dic1.items():
    if dic2.get(key, -1) != val:
        print('NO')
        break
else:
    print('YES')
