N = int(input())

mod = 10**9 + 7

ret = pow(10, N, mod) - pow(9, N, mod) * 2 + pow(8, N, mod)
print(ret % mod)
