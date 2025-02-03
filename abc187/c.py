from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]


def solve():
    mem = defaultdict(lambda: [0, 0])
    for s in S:
        if s[0] == "!":
            if mem[s[1:]][1] > 0:
                return s[1:]

            mem[s[1:]][0] += 1

        else:
            if mem[s][0] > 0:
                return s

            mem[s][1] += 1

    return "satisfiable"


print(solve())
