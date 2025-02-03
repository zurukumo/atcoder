N = int(input())

ret = 0
for i in range(1, N + 1):
    d = []
    o = []
    tmp = i
    while tmp:
        d.append(tmp % 10)
        tmp //= 10
    tmp = i
    while tmp:
        o.append(tmp % 8)
        tmp //= 8

    if 7 not in d and 7 not in o:
        ret += 1

print(ret)
