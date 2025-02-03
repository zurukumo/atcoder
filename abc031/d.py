K, N = map(int, input().split())
vw = [input().split() for _ in range(N)]


def spl(s, n):
    if n == 0:
        return [[]]

    ret = []

    m = max(len(s) - 3 * (n - 1), 1)
    M = min(len(s) - (n - 1), 3)
    for i in range(m, M + 1):
        for t in spl(s[i:], n - 1):
            ret.append([s[:i]] + t)

    return ret


for i in range(N):
    vw[i][1] = spl(vw[i][1], len(vw[i][0]))

vw.sort(key=lambda x: len(x[1]))


def rec(i, dic):
    if i == N:
        for i in range(1, K + 1):
            print(dic[i])
        exit()
    v, w = vw[i]
    for comb in w:
        flag = True
        for key, val in enumerate(comb):
            if dic[int(v[key])] != None and dic[int(v[key])] != val:
                flag = False
                break
        if flag:
            dic_ = dic.copy()
            for key, val in enumerate(comb):
                dic_[int(v[key])] = val
            rec(i + 1, dic_)

    return


rec(0, [None] * (K + 1))
