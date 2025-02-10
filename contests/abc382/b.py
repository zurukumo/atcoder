N, D = map(int, input().split())
S = input()

S = list(S)[::-1]


for _ in range(D):
    if "@" in S:
        S[S.index("@")] = "."

S = S[::-1]
print("".join(S))
