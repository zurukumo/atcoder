N = int(input())


def solve():
    for i in range(2, N):
        if N % i == 0:
            return "NO"

    return "YES"


print(solve())
