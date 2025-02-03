from collections import Counter

N = int(input())
a = [int(i) for i in input().split()]


def solve():
    c = Counter(a)
    if len(c.keys()) > 2:
        return "No"

    if len(c.keys()) == 2:
        if max(c.keys()) - min(c.keys()) != 1:
            return "No"

        mk, Mk = min(c.keys()), max(c.keys())
        mv, Mv = c[mk], c[Mk]
        n = N - mv
        m = Mk - mv
        if 0 < m * 2 <= n:
            return "Yes"
        else:
            return "No"
    else:
        n = N
        m = list(c.keys())[0]
        if m * 2 <= n or m == n - 1:
            return "Yes"
        else:
            return "No"


print(solve())
