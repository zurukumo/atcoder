S = list(input())
N = int(input())
lr = [[int(i) - 1 for i in input().split()] for _ in range(N)]

for i in range(N):
    l, r = lr[i]
    S[l : r + 1] = reversed(S[l : r + 1])

print("".join(S))
