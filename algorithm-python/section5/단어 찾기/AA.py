n = int(input())
words = set([input() for _ in range(n)])
p = dict()

for x in words:
    p[x] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
