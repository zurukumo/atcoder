N = int(input())

ret = 0
for i in range(1, N + 1):
    j = N // i
    if j < 1:
        break
    ret += (1 + j) * i * j // 2

print(ret)
