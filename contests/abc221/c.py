import itertools

N = int(input())

ns = [int(c) for c in str(N)]

ret = 0
for comb in itertools.permutations(ns):
    for i in range(1, len(ns) // 2 + 1):
        a = ""
        b = ""
        for n in comb:
            if len(a) < i:
                a += str(n)
            else:
                b += str(n)
        if a[0] == "0" or b[0] == "0":
            continue
        ret = max(ret, int(a) * int(b))

print(ret)
