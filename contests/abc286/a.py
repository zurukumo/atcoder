N, P, Q, R, S = map(int, input().split())
A = [int(i) for i in input().split()]

P -= 1
Q -= 1
R -= 1
S -= 1

A[P : Q + 1], A[R : S + 1] = A[R : S + 1], A[P : Q + 1]

print(*A)
