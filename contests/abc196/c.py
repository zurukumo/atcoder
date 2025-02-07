N = int(input())

ret = 0
for i in range(1, 10**6 + 10):
    x = int(str(i) + str(i))
    if x <= N:
        ret += 1

print(ret)
