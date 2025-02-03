N = int(input())
S = list(map(int, input()))
X = input()

S = S[::-1]
X = X[::-1]

t = set([0])
for s, x in zip(S[:-1], X[:-1]):
    tt = set([])
    if x == "A":
        for i in range(7):
            if (i * 10 + s) % 7 in t and (i * 10) % 7 in t:
                tt.add(i)
    else:
        for i in range(7):
            if (i * 10 + s) % 7 in t or (i * 10) % 7 in t:
                tt.add(i)
    t = tt


s = S[-1]
x = X[-1]
if x == "T":
    if 0 in t or (s % 7) in t:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if 0 in t and (s % 7) in t:
        print("Takahashi")
    else:
        print("Aoki")
