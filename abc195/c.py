N = int(input())

ret = 0
for i in range(3, 20, 3):
    x = max(0, N + 1 - 10**i)
    ret += x

print(ret)
