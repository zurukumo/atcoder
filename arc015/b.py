N = int(input())
Mm = [[float(i) for i in input().split()] for _ in range(N)]

ret = [0] * 6

for M, m in Mm:
    if 35 <= M:
        ret[0] += 1
    if 30 <= M < 35:
        ret[1] += 1
    if 25 <= M < 30:
        ret[2] += 1
    if 25 <= m:
        ret[3] += 1
    if m < 0 and 0 <= M:
        ret[4] += 1
    if M < 0:
        ret[5] += 1

print(*ret)
