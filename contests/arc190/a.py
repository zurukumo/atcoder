N, M = map(int, input().split())
LR = [[int(i) for i in input().split()] for _ in range(M)]


def solve():
    lri = [(l, r, i) for i, (l, r) in enumerate(LR)]
    ret = [0] * M

    # 一発で行けるやつ
    for l, r, i in lri:
        if l == 1 and r == N:
            ret[i] = 1
            print(1)
            print(*ret)
            return

    # 左端と右端でかぶるやつ
    left_r = 0
    left_i = -1
    right_l = N + 1
    right_i = -1
    for l, r, i in lri:
        if l == 1:
            if r > left_r:
                left_r = r
                left_i = i

        if r == N:
            if l < right_l:
                right_l = l
                right_i = i
    if left_r >= right_l:
        ret[left_i] = 1
        ret[right_i] = 1
        print(2)
        print(*ret)
        return

    # 一方が一方を完全に含むやつ
    lri.sort(key=lambda x: (x[0], -x[1]))
    max_r = -float("inf")
    max_i = -1
    for _, r, i in lri:
        if r <= max_r:
            ret[i] = 2
            ret[max_i] = 1
            print(2)
            print(*ret)
            return
        if r > max_r:
            max_r = r
            max_i = i

    # 完全に被ってないやつ
    right_l = -1
    right_i = -1
    for l, r, i in lri:
        if l > right_l:
            right_l = l
            right_i = i
    for l, r, i in lri:
        if r < right_l:
            ret[i] = 2
            ret[right_i] = 2
            print(2)
            print(*ret)
            return

    # 3つズレているとき
    for i in range(M - 3):
        l1, r1, i1 = lri[i]
        l2, r2, i2 = lri[i + 1]
        l3, r3, i3 = lri[i + 2]
        if l1 < l2 < l3 and r1 < r2 < r3:
            ret[i1] = 1
            ret[i2] = 2
            ret[i3] = 1
            print(3)
            print(*ret)
            return

    print(-1)


solve()
