N, M = map(int, input().split())

mod = 998244353
same, diff = M, 0
for i in range(1, N):
    same, diff = diff, (same * (M - 1) + diff * (M - 2)) % mod

print(diff)
