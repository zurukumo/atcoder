N, K = map(int, input().split())
A = [int(i) for i in input().split()]


def solve():
    if N == 2 and A[0] > A[1] and A[0] - A[1] < K:
        print("No")
        return

    ret = []
    for i in range(N - 1):
        while (
            (i - 1 >= 0 and A[i - 1] > A[i])
            or (i - 1 >= 0 and A[i - 1] > A[i + 1])
            or (i + 2 < N and abs(A[i + 1] - A[i + 2]) < K)
            or (i == N - 2 and A[i] > A[i + 1])
        ):
            ret.append(i + 1)
            A[i], A[i + 1] = A[i + 1] + K, A[i]

    print("Yes")
    print(len(ret))
    print(*ret)


solve()
