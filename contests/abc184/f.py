N, T = map(int, input().split())
A = [int(i) for i in input().split()]


def solve():
    if len(A) <= 4:
        ret = 0
        for mask in range(1 << len(A)):
            x = 0
            for i in range(len(A)):
                if (1 << i) & mask:
                    x += A[i]
            if x <= T:
                ret = max(ret, x)

        return ret

    ret = 0
    a = []
    b = []
    c = []
    d = []
    L = len(A) // 4
    R = len(A) - 3 * L
    for mask in range(1 << L):
        w = 0
        x = 0
        y = 0
        for i in range(L):
            if (1 << i) & mask:
                w += A[i]
                x += A[i + L]
                y += A[i + L * 2]
        if w <= T:
            a.append(w)
        if x <= T:
            b.append(x)
        if y <= T:
            c.append(y)

    for mask in range(1 << R):
        z = 0
        for i in range(R):
            if (1 << i) & mask:
                z += A[i + L * 3]
        if z <= T:
            d.append(z)

    wx = []
    for w in a:
        for x in b:
            if w + x <= T:
                wx.append(w + x)

    yz = []
    for y in c:
        for z in d:
            if y + z <= T:
                yz.append(y + z)

    wx.sort()
    yz.sort()

    i = len(yz) - 1
    for j in wx:
        while j + yz[i] > T:
            i -= 1
        ret = max(ret, j + yz[i])

    return ret


print(solve())
