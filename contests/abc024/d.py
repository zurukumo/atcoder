A = int(input())
B = int(input())
C = int(input())
MOD = 10**9 + 7

x = (A * (B + C) - B * C) % MOD
inv = pow(x, MOD - 2, MOD)

c = B * (C - A) * inv % MOD
r = C * (B - A) * inv % MOD

print(r, c)
