S = input() + '#'
M = 0
ret = 0
for s in S :
    if s in 'AGCT' :
        ret += 1
    else :
        M = max(M, ret)
        ret = 0
print(M)