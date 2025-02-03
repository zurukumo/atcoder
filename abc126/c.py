N, K = map(int, input().split())

exp = 0


def calc_exp(init):
    point = init
    n_play = 0

    while point < K:
        point *= 2
        n_play += 1

    return 1 / (2**n_play)


for i in range(1, N + 1):
    exp += calc_exp(i)

print("{:.10f}".format(exp / N))
