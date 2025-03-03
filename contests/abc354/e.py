N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]


mem = dict()


def dfs(v):
    if v in mem:
        return mem[v]

    s = 0
    for i in range(N):
        if v & 1 << i:
            continue
        for j in range(i + 1, N):
            if v & 1 << j:
                continue
            if AB[i][0] == AB[j][0] or AB[i][1] == AB[j][1]:
                s |= 1 - dfs(v | 1 << i | 1 << j)

    mem[v] = s
    return s


if dfs(0):
    print("Takahashi")
else:
    print("Aoki")
