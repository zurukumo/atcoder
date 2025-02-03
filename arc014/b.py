N = int(input())
W = [input() for _ in range(N)]


def solve():
    for i in range(1, N):
        if W[i][0] != W[i - 1][-1] or W[i] in W[:i]:
            if i % 2 == 0:
                return "LOSE"
            else:
                return "WIN"

    return "DRAW"


print(solve())
