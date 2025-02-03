T = int(input())


def solve(N, A):
    s = sum(A)
    while len(A) >= 2:
        a = A.pop()
        s -= a
        c = (a * len(A) - s) // (1 + len(A))
        s += c
        A[-1] += c
        if c < 0:
            return "No"

    return "Yes"


for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]

    print(solve(N, A))
