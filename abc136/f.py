from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]
xy.sort()

ylist = [y for _, y in xy]
ylist.sort()
for i in range(N) :
    xy[i] = [i, bisect_left(ylist, xy[i][1])]

MOD = 998244353

def bit_sum(i) :
    s = 0
    while i > 0 :
        s += bit[i]
        i -= i & -i
    return s

def bit_add(i, x) :
    while i <= N :
        bit[i] += x
        i += i & -i

lu = [0] * N
ld = [0] * N
ru = [0] * N
rd = [0] * N

power = [1]
for _ in range(N) :
    power.append(power[-1] * 2 % MOD)

bit = [0] * (N + 1)
for i, (x, y) in enumerate(xy) :
    ld[i] = bit_sum(y+1)
    lu[i] = i - ld[i]
    bit_add(y+1, 1)

bit = [0] * (N + 1)
for i, (x, y) in enumerate(xy[::-1]) :
    rd[N-i-1] = bit_sum(y+1)
    ru[N-i-1] = i - rd[N-i-1]
    bit_add(y+1, 1)

ret = 0
for i in range(N) :
    ret += (power[lu[i]]-1)*power[ld[i]]*power[ru[i]]*(power[rd[i]]-1)
    ret += power[lu[i]]*(power[ld[i]]-1)*(power[ru[i]]-1)*power[rd[i]]
    ret -= (power[lu[i]]-1)*(power[ld[i]]-1)*(power[ru[i]]-1)*(power[rd[i]]-1)
    ret += power[lu[i]] * power[ld[i]] * power[ru[i]] * power[rd[i]]
    ret %= MOD
    
print(ret)