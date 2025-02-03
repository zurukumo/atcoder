import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

setT = set(T)
lenS = sum(len(s) for s in S)


def partition(n, m):
    def helper(remaining, parts):
        if parts == 0:
            yield []
        if parts == 1:
            for i in range(1, remaining + 1):
                yield [i]
            return
        for i in range(1, remaining + 1):
            for rest in helper(remaining - i, parts - 1):
                yield [i] + rest

    return helper(n, m)


for underbar in partition(16 - lenS, N - 1):
    for permS in itertools.permutations(S):
        joinedS = ""
        for i in range(N):
            joinedS += permS[i]
            if i != N - 1:
                joinedS += "_" * underbar[i]

        if not 3 <= len(joinedS) <= 16:
            continue

        if not joinedS in setT:
            print(joinedS)
            exit()


print(-1)
