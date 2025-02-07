from itertools import product

N, M = map(int, input().split())

ks = [[int(i) for i in input().split()] for _ in range(M)]
p = [int(i) for i in input().split()]

res = 0

for i in product(range(2), repeat=N):
    flag = True
    for j in range(M):
        tmp = 0
        for s in ks[j][1:]:
            tmp += i[s - 1]

        if tmp % 2 != p[j]:
            flag = False
            break
    if flag:
        res += 1

print(res)
