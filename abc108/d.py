L = int(input())
  
ret = []
count = 0
for i in range(19, 0, -1) :
    while L - (1 << (i - 1)) >= 0 :
        ret.append((i, count))
        count += 1 << (i - 1)
        L -= 1 << (i - 1)

N = ret[0][0]
M = len(ret) + 2 * (N - 1)

print(N + 1, M)
for i in range(1, N) :
    print(i, i + 1, 0)
    print(i, i + 1, 1 << (i - 1))
for r in ret :
    print(r[0], N + 1, r[1])