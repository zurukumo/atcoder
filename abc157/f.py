N, K = map(int, input().split())
xyc = [[int(i) for i in input().split()] for _ in range(N)]


def check(n):
    for i in range(N):
        xi, yi, ci = xyc[i]
        ri = n / ci
        for j in range(i + 1, N):
            xj, yj, cj = xyc[j]
            xj -= xi
            yj -= yi
            rj = n / cj
            a = (xj**2 + yj**2 + ri**2 - rj**2) / 2
            root = max(0, (xj**2 + yj**2) * (ri**2) - a**2) ** 0.5
            for sgn in [1, -1]:
                cnt = 0
                X = (a * xj + sgn * yj * root) / (xj**2 + yj**2) + xi
                Y = (a * yj - sgn * xj * root) / (xj**2 + yj**2) + yi
                for x, y, c in xyc:
                    if (x - X) ** 2 + (y - Y) ** 2 <= (n / c) ** 2 + eps:
                        cnt += 1
                if cnt >= K:
                    return True

    for X, Y, _ in xyc:
        cnt = 0
        for x, y, c in xyc:
            if (x - X) ** 2 + (y - Y) ** 2 <= (n / c) ** 2 + eps:
                cnt += 1
        if cnt >= K:
            return True

    return False


eps = 1e-8
ng, ok = 0, 10**6
while ok - ng > eps:
    n = (ng + ok) / 2
    if check(n):
        ok = n
    else:
        ng = n

print(ok)
