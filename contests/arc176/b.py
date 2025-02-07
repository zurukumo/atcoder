T = int(input())
NMK = [[int(i) for i in input().split()] for _ in range(T)]

for n, m, k in NMK:
    if n > m:
        c = (n - m) // (m - k)
        n -= (c + 1) * (m - k)
    if n == m - 1 and k == m - 1:
        print(0)
    else:
        print(pow(2, n, 10))
