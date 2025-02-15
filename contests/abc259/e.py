N = int(input())
pes = [[] for _ in range(N)]

max_mem = dict()

for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        if p in max_mem:
            if max_mem[p][0] < e:
                max_mem[p] = (e, 1)
            elif max_mem[p][0] == e:
                max_mem[p] = (e, max_mem[p][1] + 1)
        else:
            max_mem[p] = (e, 1)
        pes[i].append((p, e))

ret = 0
none = 0
for pe in pes:
    for p, e in pe:
        if max_mem[p][0] == e and max_mem[p][1] == 1:
            ret += 1
            break
    else:
        none = 1

print(ret + none)
