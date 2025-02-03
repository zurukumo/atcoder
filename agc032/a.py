N = int(input())

ret = []
for i in range(1, N + 1) :
    for j in range(i + 1, N + 1) :
        if N % 2 == 0 and i + j == N + 1 :
            continue
        if N % 2 == 1 and i + j == N :
            continue
        ret.append((i, j))

print(len(ret))
for r in ret :
    print(*r)
