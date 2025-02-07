from itertools import product

N, K = map(int, input().split())
T = [[int(i) for i in input().split()] for _ in range(N)]


def check():
    for i in product(range(K), repeat=N):
        res = 0
        for k, v in enumerate(i):
            res ^= T[k][v]

        if res == 0:
            return "Found"

    return "Nothing"


print(check())
