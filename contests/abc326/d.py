N = int(input())
R = input()
C = input()


T = [["."] * N for _ in range(N)]
col = [set() for _ in range(N)]
row = [set() for _ in range(N)]


def dfs(y, x, s):
    if y == N:
        if s == 3 * N:
            print("Yes")
            for t in T:
                print("".join(t))
            exit()
        else:
            return

    if y > 0 and len(row[y - 1]) != 3:
        return

    candidates = set(["A", "B", "C"])
    if len(row[y]) == 0:
        candidates &= set(R[y])
    if len(row[y]) > 0:
        candidates -= row[y]
    if len(col[x]) == 0:
        candidates &= set(C[x])
    if len(col[x]) > 0:
        candidates -= col[x]

    ny, nx = y, x + 1
    if nx == N:
        nx = 0
        ny += 1

    for c in candidates:
        T[y][x] = c
        row[y].add(c)
        col[x].add(c)
        dfs(ny, nx, s + 1)
        row[y].remove(c)
        col[x].remove(c)
        T[y][x] = "."
    dfs(ny, nx, s)


dfs(0, 0, 0)

print("No")
