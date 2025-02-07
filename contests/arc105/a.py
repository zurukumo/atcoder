x = [int(i) for i in input().split()]


def solve():
    for i in range(1 << 4):
        a = 0
        b = 0
        for j in range(4):
            if i & (1 << j):
                a += x[j]
            else:
                b += x[j]

        if a == b:
            return "Yes"

    return "No"


print(solve())
