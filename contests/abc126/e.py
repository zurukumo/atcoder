N, M = map(int, input().split())

parent = [-1] * (N + 1)


def root(x):
    while parent[x] >= 0:
        x = parent[x]
    return x


def unite(x, y):
    root_x = root(x)
    root_y = root(y)

    if root_x != root_y:
        if parent[root_x] > parent[root_y]:
            parent[root_x] = root_y
        else:
            if parent[root_x] == parent[root_y]:
                parent[root_x] -= 1
            parent[root_y] = root_x

    return


for _ in range(M):
    X, Y, Z = map(int, input().split())
    unite(X, Y)

print(sum(i < 0 for i in parent) - 1)
