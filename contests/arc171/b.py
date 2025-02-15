N = int(input())
A = [int(i) - 1 for i in input().split()]

mod = 998244353

ret = 1
n = set()
removed = 0
for i in range(N):
    n.add(A[i])
    if i == A[i]:
        ret *= len(n) - removed
        ret %= mod
        removed += 1
    if i > A[i]:
        ret *= 0
    if A[A[i]] != A[i]:
        ret *= 0

print(ret)
