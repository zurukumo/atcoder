N, S, D = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]


def judge():
    for X, Y in XY:
        if X < S and Y > D:
            return 'Yes'

    return 'No'


print(judge())
