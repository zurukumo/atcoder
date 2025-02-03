N = int(input())
S = input()
A = [int(i) for i in input().split()]

k = min(abs(A[i] - A[i + 1]) for i in range(N))


def solve(N, S, A):
    k = min(abs(A[i] - A[i + 1]) for i in range(N))

    B = [[0] * (N + 1) for _ in range(k)]
    for i in range(k):
        for j in range(N + 1):
            c = A[j] // k
            d = c * k + k - A[j]
            if i < d:
                B[i][j] = c
            else:
                B[i][j] = c + 1

    return k, B


k, B = solve(N, S, A)
print(k)
for row in B:
    print(*row)
