from itertools import permutations

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

ret = 0
for p, q, r in permutations((P, Q, R)):
    ret = max(ret, (N // p) * (M // q) * (L // r))
print(ret)
