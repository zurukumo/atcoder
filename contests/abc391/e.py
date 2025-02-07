import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = input()


def dfs1(l, r):
    if r - l == 3:
        if A[l:r].count("1") == 0:
            return 2
        elif A[l:r].count("1") == 1:
            return 1
        else:
            return 0

    block = (r - l) // 3
    acost = dfs1(l, l + block)
    bcost = dfs1(l + block, l + 2 * block)
    ccost = dfs1(l + 2 * block, r)

    return sum([acost, bcost, ccost]) - max(acost, bcost, ccost)


def dfs2(l, r):
    if r - l == 3:
        if A[l:r].count("0") == 0:
            return 2
        elif A[l:r].count("0") == 1:
            return 1
        else:
            return 0

    block = (r - l) // 3
    acost = dfs2(l, l + block)
    bcost = dfs2(l + block, l + 2 * block)
    ccost = dfs2(l + 2 * block, r)

    return sum([acost, bcost, ccost]) - max(acost, bcost, ccost)


a = dfs1(0, 3**N)
b = dfs2(0, 3**N)
print(max(a, b))
