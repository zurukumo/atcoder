H, W, Const = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]


def solve():
    B = [[-float("inf")] * W for _ in range(H)]
    C = [[-float("inf")] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            B[y][x] = -A[y][x] + Const * (y + x)

    # print()
    # for b_ in B:
    # print(b_)

    for y in range(H):
        for x in range(W):
            if y - 1 >= 0:
                C[y][x] = max(C[y][x], C[y - 1][x], B[y - 1][x])
            if x - 1 >= 0:
                C[y][x] = max(C[y][x], C[y][x - 1], B[y][x - 1])

    # print()
    # for c_ in C:
    # print(c_)

    ret = float("inf")
    for y in range(H):
        for x in range(W):
            ret = min(ret, A[y][x] + Const * (y + x) - C[y][x])

    return ret


a = solve()
for y in range(H):
    A[y] = A[y][::-1]
b = solve()
print(min(a, b))
