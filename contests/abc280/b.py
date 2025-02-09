N = int(input())
S = [int(i) for i in input().split()]

ret = [S[0]]
for i in range(1, N):
    ret.append(S[i] - S[i - 1])

print(*ret)
