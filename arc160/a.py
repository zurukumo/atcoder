T = int(input())
N = [int(input()) for _ in range(T)]

mod = 998244353


for n in N:
    ret = 0
    for y in range(1, n + 1):
        if y * y > n:
            break
        z_max = n // y
        if z_max >= y:
            ret += (z_max - y + 1) * y * 6 % mod
            # yとzが同じ場合を引く
            ret -= y * 3
            # xとyが同じ場合を引く
            ret -= (z_max - y + 1) * 3
            # xとyとzが同じ場合を足す
            ret += 1
        ret %= mod
    print(ret)
