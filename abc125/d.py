N = int(input())
A = list(map(int, input().split()))

p = 0
m = float("inf")
ret = 0
for a in A:
    if a < 0:
        p ^= 1
        m = min(m, -a)
        ret -= a
    else:
        m = min(m, a)
        ret += a

if p == 0:
    print(ret)
else:
    print(ret - 2 * m)
