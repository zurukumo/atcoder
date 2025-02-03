N = int(input())
b = [int(i) for i in input().split()]


def solve():
    ret = []
    while len(b) != 0:
        M = -1
        for i in range(len(b)):
            if i + 1 == b[i]:
                M = i

        if M == -1:
            print(-1)
            return

        ret.append(b.pop(M))

    for r in ret[::-1]:
        print(r)


solve()
