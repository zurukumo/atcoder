N = int(input())

ret = 0
for i in range(1, N + 1, 2):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 8:
        ret += 1
print(ret)
