from collections import Counter

N, M = map(int, input().split())
name = input()
kit = input()

cn = Counter(name)
ck = Counter(kit)

ret = 0
for k in cn.keys():
    if ck[k] == 0:
        ret = -1
        break

    ret = max(ret, (cn[k] + ck[k] - 1) // ck[k])

print(ret)
