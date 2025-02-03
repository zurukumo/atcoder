N, A, B = map(int, input().split())
a = [int(i) for i in input().split()]

mod = 10**9 + 7

if A != 1:
    while B > 0 and min(a) * A <= max(a):
        i = a.index(min(a))
        a[i] *= A
        B -= 1
else:
    B = 0

a.sort()
for i in range(B % N, B % N + N):
    i = i % N
    print(a[i] * pow(A, (B - i - 1) // N + 1, mod) % mod)
