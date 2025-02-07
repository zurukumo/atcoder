C = int(input())
NML = [sorted([int(i) for i in input().split()]) for _ in range(C)]

Nmax, Mmax, Lmax = 0, 0, 0
for N, M, L in NML:
    Nmax = max(Nmax, N)
    Mmax = max(Mmax, M)
    Lmax = max(Lmax, L)

print(Nmax * Mmax * Lmax)
