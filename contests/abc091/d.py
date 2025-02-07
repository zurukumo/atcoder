from bisect import bisect_left

N = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

ret = 0
c = 1 << 28
for i in range(28, -1, -1):
    for j in range(N):
        a[j] &= (1 << (i + 1)) - 1
        b[j] &= (1 << (i + 1)) - 1
    a.sort()
    b.sort()

    bit = 0
    k, l, m, n = N - 1, N - 1, N - 1, N - 1
    for j in range(N):
        while k > 0 and a[k] > 1 * c - a[j]:
            k -= 1
        while l > 0 and a[l] > 2 * c - a[j]:
            l -= 1
        while m > 0 and a[m] > 3 * c - a[j]:
            m -= 1
        while n > 0 and a[n] > 4 * c - a[j]:
            n -= 1
        bit ^= (bisect_left(b, 2 * c - a[j]) - bisect_left(b, 1 * c - a[j])) & 1
        bit ^= (bisect_left(b, 4 * c - a[j]) - bisect_left(b, 3 * c - a[j])) & 1
    ret <<= 1
    ret |= bit
    c >>= 1

print(ret)
