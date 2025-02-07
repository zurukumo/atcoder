N = int(input())
A = [int(i) for i in input().split()]

A.sort()
S = [A[0]]
for i in range(1, N):
    S.append(S[-1] + A[i])

for i in range(N - 2, -1, -1):
    if A[i] > S[i - 1] * 2:
        break

print(N - i)
