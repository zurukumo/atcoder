S = input()
mod = 10 ** 9 + 7

ret = 0
la, rc = 0, S.count('C')
lq, rq = 0, S.count('?')

def comb(ac, q) :
    if q == 0 :
        return ac * pow(3, q, mod) % mod
    else :
        p = pow(3, q - 1, mod)
        return (q * p + ac * p * 3) % mod

for s in S :
    if s == '?' :
        rq -= 1
        ret += comb(la, lq) * comb(rc, rq)
        ret %= mod
        lq += 1
    elif s == 'A' :
        la += 1
    elif s == 'B' :
        ret += comb(la, lq) * comb(rc, rq)
        ret %= mod
    elif s == 'C' :
        rc -= 1
    
print(ret)