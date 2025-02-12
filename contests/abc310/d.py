N, T, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

ng_list = [0] * N
for a, b in AB:
    ng_list[a - 1] |= 1 << (b - 1)
    ng_list[b - 1] |= 1 << (a - 1)


def dfs(groups, i):
    if i == N:
        if all(groups):
            return 1
        else:
            return 0

    s = 0
    for j in range(T):
        if groups[j] & ng_list[i] == 0:
            groups[j] |= 1 << i
            s += dfs(groups, i + 1)
            groups[j] &= ~(1 << i)
        if groups[j] == 0:
            break
    return s


print(dfs([0] * T, 0))
