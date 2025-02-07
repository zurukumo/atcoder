N = int(input())
tlr = [[int(i) * 10 for i in input().split()] for _ in range(N)]

for i in range(N):
    t, l, r = tlr[i]
    t //= 10

    if t == 2 or t == 4:
        tlr[i][2] -= 1
    if t == 3 or t == 4:
        tlr[i][1] += 1

ret = 0
for i in range(N):
    ti, li, ri = tlr[i]
    for j in range(i + 1, N):
        tj, lj, rj = tlr[j]
        if li <= lj <= ri or li <= rj <= ri or lj <= li <= rj or lj <= ri <= rj:
            ret += 1

print(ret)
