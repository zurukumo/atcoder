X = input()
N = int(input())
S = [input() for _ in range(N)]

T = []

for s in S:
    t = ""
    for c in s:
        t += chr(ord("a") + X.index(c))
    T.append(t)

st = zip(S, T)
for s, t in sorted(st, key=lambda x: x[1]):
    print(s)
