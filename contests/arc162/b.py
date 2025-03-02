N = int(input())
P = [int(i) for i in input().split()]

s = 0
for i in range(N):
    for j in range(i + 1, N):
        if P[i] > P[j]:
            s += 1

if s % 2 == 1:
    print("No")
    exit()

ret = []
i = 0
while i < N and len(ret) < 2000:
    if P[i] == i + 1:
        i += 1
        continue

    iidx = P.index(i + 1)
    if iidx != N - 1:
        s = P[iidx : iidx + 2]
        P = P[:iidx] + P[iidx + 2 :]
        P = P[:i] + s + P[i:]
        ret.append((iidx + 1, i))
        i += 1
    else:
        for m in range(N, 0, -1):
            midx = P.index(m)
            if midx != N - 1 and midx + 1 != iidx:
                s = P[midx : midx + 2]
                P = P[:midx] + P[midx + 2 :] + s
                ret.append((midx + 1, N - 2))
                break

print("Yes")
print(len(ret))
for r in ret:
    print(*r)
