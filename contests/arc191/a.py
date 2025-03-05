N, M = map(int, input().split())
S = input()
T = input()

S = list(S)
T = list(T)

last_t = T[-1]
T.sort()

min_update = "9"

for i in range(N):
    if T and T[-1] >= S[i]:
        min_update = min(min_update, T[-1])
    if T and T[-1] > S[i]:
        S[i] = T.pop()

if min_update > last_t:
    S[-1] = last_t

print("".join(S))
