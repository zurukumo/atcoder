from bisect import bisect_right

N, A, B = map(int, input().split())
v = [int(i) for i in input().split()]
v.sort(reverse=True)

def comb(n, r) :
    if n == 0 or r == 0 :
        return 0
    ret = 1
    for i in range(1, n+1) :
        ret *= i
    for i in range(1, r+1) :
        ret //= i
    for i in range(1, n-r+1) :
        ret //= i
    return ret

print(sum(v[:A])/A)

if v[A-1] != v[0] :
    ret = 0
    a = v.count(v[A-1])
    r = v[:A].count(v[A-1])
    print(comb(a, r))

else :
    a = v.count(v[A-1])
    ret = 0
    for i in range(A, min(B, a) + 1) :
        ret += comb(a, i)
    print(ret)