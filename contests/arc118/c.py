N = int(input())

ret = [3 * 5 * 7]
i = 1
while len(ret) < N:
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        ret.append(2 * i)
    i += 1

print(*ret)
