N, M, X, Y = map(int, input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]


def check():
    for Z in range(max(x) + 1, min(y) + 1):
        if X < Z <= Y:
            return "No War"

    return "War"


print(check())
