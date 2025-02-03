n = int(input())
S = [input() for _ in range(n)]

ret = []
S0 = set(S[0])

for c in S0:
    m = float("inf")
    for i in range(n):
        m = min(m, S[i].count(c))
    ret.append((c, m))

ret.sort()
T = []

for c, m in ret:
    if m > 0:
        for _ in range(m):
            T.append(c)

print("".join(T))
