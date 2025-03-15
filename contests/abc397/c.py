N = int(input())
A = [int(i) for i in input().split()]

dpl = [0] * N
dpr = [0] * N

s = set()
for i in range(N):
    s.add(A[i])
    dpl[i] = len(s)

s = set()
for i in range(N - 1, -1, -1):
    s.add(A[i])
    dpr[i] = len(s)

print(max(dpl[i] + dpr[i + 1] for i in range(N - 1)))
