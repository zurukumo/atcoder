N, X = map(int, input().split())
L = [int(i) for i in input().split()]

D = 0
ret = 1
for l in L:
    D += l
    if D <= X:
        ret += 1
    else:
        break
print(ret)
