X = int(input())

ret = 0
cur = 100
while cur < X:
    cur += cur // 100
    ret += 1

print(ret)
