N, C = map(int, input().split())
stc = [[int(i) for i in input().split()] for _ in range(N)]
stc.append([float('inf')] * 3)

stc.sort()
stc.sort(key=lambda x: x[2])

imos = [0] * (10 ** 5 + 2)
ps, pt, pc = stc[0]
for i in range(1, N + 1) :
    if stc[i][0] == pt and stc[i][2] == pc :
        pt = stc[i][1]
    else :
        imos[ps] += 1
        imos[pt+1] -= 1
        ps, pt, pc = stc[i]
    
for i in range(1, 10 ** 5 + 2) :
    imos[i] += imos[i-1]

print(max(imos))