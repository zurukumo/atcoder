N = int(input())
N_ = N

parity = 0
while N_ > 0 :
    N_ //= 2
    parity ^= 1
c = 1 
parity_ = parity
while c <= N :
    c = 2 * c + parity_
    parity_ ^= 1
print(['Takahashi', 'Aoki'][parity^parity_])
    