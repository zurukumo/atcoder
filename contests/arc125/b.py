N = int(input())


mod = 998244353

ret = 0
for a in range(1, 10**10):
    if a * a > N:
        break
    b = N // a
    if a % 2 != b % 2:
        b -= 1
    ret += (b - a) // 2 + 1
    ret %= mod

print(ret)
