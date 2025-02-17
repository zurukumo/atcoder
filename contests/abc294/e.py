L, N1, N2 = map(int, input().split())
vl1 = [[int(i) for i in input().split()] for _ in range(N1)]
vl2 = [[int(i) for i in input().split()] for _ in range(N2)]

i = 0
j = 0
ret = 0
while i < N1 and j < N2:
    vi, li = vl1[i]
    vj, lj = vl2[j]

    if vi == vj:
        ret += min(li, lj)

    li, lj = li - min(li, lj), lj - min(li, lj)
    vl1[i][1] = li
    vl2[j][1] = lj
    if li == 0:
        i += 1
    if lj == 0:
        j += 1

print(ret)
