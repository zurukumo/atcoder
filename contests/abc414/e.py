import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

mod = 998244353
ret = (N - 1) * N * pow(2, mod - 2, mod) % mod

i = 1
while True:
    if i**2 > N:
        break
    ret -= N // i - 1
    ret %= mod
    i += 1

d = N // i
while d > 0:
    ret -= (N // d - N // (d + 1)) * (d - 1)
    ret %= mod
    d -= 1

print(ret)
