from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

cnt = Counter(S)
M = max(cnt.values())

ret = []
for k, v in cnt.items():
    if v == M:
        ret.append(k)

ret.sort()
for r in ret:
    print(r)
