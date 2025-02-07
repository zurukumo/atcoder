# ikatakosさんの提出を見てlru_cacheなるものを知った。
# まだまだ知らないことがたくさんありますね。

from functools import lru_cache

N = int(input())
A = [int(i) for i in input().split()]


@lru_cache(maxsize=None)
def rec(l, r, xl, xr):
    if l + 1 == r:
        return 0

    return min(
        rec(l, m, xl, xl + xr) + rec(m, r, xl + xr, xr) + A[m] * (xl + xr)
        for m in range(l + 1, r)
    )


print(A[0] + rec(0, N - 1, 1, 1) + A[N - 1])
