X, Y = map(int, input().split())

ret = 0
while X <= Y:
    X *= 2
    ret += 1
print(ret)
