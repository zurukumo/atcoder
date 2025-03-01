import math

N, a, b, c = map(int, input().split())
A = [int(i) for i in input().split()]

alist = []
blist = []
clist = []
ablist = []
bclist = []
calist = []
abclist = []


def calc(x, fac):
    if x % fac == 0:
        return 0
    return fac - x % fac


for i in range(N):
    alist.append((calc(A[i], a), i))
    blist.append((calc(A[i], b), i))
    clist.append((calc(A[i], c), i))
    ablist.append((calc(A[i], math.lcm(a, b)), i))
    bclist.append((calc(A[i], math.lcm(b, c)), i))
    calist.append((calc(A[i], math.lcm(c, a)), i))
    abclist.append((calc(A[i], math.lcm(a, b, c)), i))


def find_3min(arr):
    mv1, mv2, mv3 = float("inf"), float("inf"), float("inf")
    mk1, mk2, mk3 = None, None, None
    for v, k in arr:
        if v < mv1:
            mv3, mk3 = mv2, mk2
            mv2, mk2 = mv1, mk1
            mv1, mk1 = v, k
        elif v < mv2:
            mv3, mk3 = mv2, mk2
            mv2, mk2 = v, k
        elif v < mv3:
            mv3, mk3 = v, k

    ret = []
    if mk1 is not None:
        ret.append((mv1, mk1))
    if mk2 is not None:
        ret.append((mv2, mk2))
    if mk3 is not None:
        ret.append((mv3, mk3))
    return ret


alist = find_3min(alist)[:3]
blist = find_3min(blist)[:3]
clist = find_3min(clist)[:3]
ablist = find_3min(ablist)[:2]
bclist = find_3min(bclist)[:2]
calist = find_3min(calist)[:2]
abclist = find_3min(abclist)[:1]

ret = abclist[0][0]
for av, ak in alist:
    for bv, bk in blist:
        for cv, ck in clist:
            if ak != bk and bk != ck and ck != ak:
                ret = min(ret, av + bv + cv)

for abv, abk in ablist:
    for cv, ck in clist:
        if abk != ck:
            ret = min(ret, abv + cv)

for bcv, bck in bclist:
    for av, ak in alist:
        if bck != ak:
            ret = min(ret, bcv + av)

for cav, cak in calist:
    for bv, bk in blist:
        if cak != bk:
            ret = min(ret, cav + bv)

print(ret)
