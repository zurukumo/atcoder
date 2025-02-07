N, K = map(int, input().split())
S = input() + "2"

T = []
c = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        c += 1
    else:
        T.append(c)
        c = 1

for i in range(1, len(T)):
    T[i] += T[i - 1]

if S[-2] == "0":
    T.append(T[-1])

ret = 0
for i in range(0 if S[0] == "1" else 1, len(T), 2):
    if i - 2 * K - 1 < 0:
        ret = max(ret, T[i])
    else:
        ret = max(ret, T[i] - T[i - 2 * K - 1])

print(ret)
